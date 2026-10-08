#!/bin/bash
# Setup a book-storage VPS: nginx + php-fpm + downloader, ready to serve + download books.
# Run as root on a fresh Ubuntu/Debian VPS.
set -e

echo "=== updating system ==="
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq nginx php-fpm php-cli curl wget python3 ca-certificates > /dev/null

echo "=== create book storage dir ==="
mkdir -p /srv/books/downloads
chown -R www-data:www-data /srv/books

echo "=== nginx config: serve /srv/books/downloads at :8080 ==="
cat > /etc/nginx/sites-available/books << 'EOF'
server {
    listen 8080;
    server_name _;
    root /srv/books/downloads;
    index index.html;
    autoindex off;

    # No directory listing - we only serve files by exact name
    location / {
        try_files $uri =404;
    }
    # API for the library (metadata)
    location ~ ^/api/ {
        fastcgi_pass unix:/run/php/php-fpm.sock;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }
    # Block .htaccess etc
    location ~ /\. { deny all; }
}
EOF
ln -sf /etc/nginx/sites-available/books /etc/nginx/sites-enabled/books
rm -f /etc/nginx/sites-enabled/default

echo "=== php-fpm socket path ==="
# find php-fpm version
PHPVER=$(ls /usr/sbin/php-fpm* 2>/dev/null | head -1 | grep -oE '[0-9]+\.[0-9]+' || echo "8.1")
echo "PHP version: $PHPVER"
# ensure php-fpm listens on the socket we reference
FPMCONF=$(ls /etc/php/$PHPVER/fpm/pool.d/www.conf 2>/dev/null || ls /etc/php/*/fpm/pool.d/www.conf 2>/dev/null | head -1)
if [ -n "$FPMCONF" ]; then
    sed -i 's|listen = .*|listen = /run/php/php-fpm.sock|' "$FPMCONF"
    sed -i 's|listen.owner = .*|listen.owner = www-data|' "$FPMCONF"
    sed -i 's|listen.group = .*|listen.group = www-data|' "$FPMCONF"
    sed -i 's|listen.mode = .*|listen.mode = 0660|' "$FPMCONF"
fi

echo "=== restart services ==="
nginx -t && systemctl restart nginx || service nginx restart
systemctl restart php$PHPVER-fpm 2>/dev/null || service php$PHPVER-fpm restart 2>/dev/null || service php-fpm restart 2>/dev/null || true

echo "=== firewall: open 8080 ==="
ufw allow 8080/tcp 2>/dev/null || true

echo "=== done. VPS book storage ready ==="
echo "Serving /srv/books/downloads on :8080"
df -h /srv | tail -1
