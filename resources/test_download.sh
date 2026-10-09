#!/bin/bash
# Quick foreground test: download 2 files to confirm pipeline works
cd /home/USER/books/downloads || exit 1
head -2 /home/USER/books/download_manifest.txt > /tmp/test_manifest.txt
echo "test manifest:"
cat /tmp/test_manifest.txt
echo "=== running 2-worker download ==="
awk -F'\t' '{print $1 "\t" $2}' /tmp/test_manifest.txt | xargs -P 2 -n 2 bash -c 'wget -q -c -L -T 60 -t 3 -U "Mozilla/5.0" -O "$0.tmp" "$1" && mv "$0.tmp" "$0" && echo "OK $0" || { rm -f "$0.tmp"; echo "FAIL $0"; }'
echo "=== result ==="
ls -la
