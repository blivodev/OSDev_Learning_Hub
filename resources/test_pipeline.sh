#!/bin/bash
# Full pipeline test: run download_books.sh logic on 3 real files
set -u
WORKERS=3
LOGFILE=/tmp/pipe_test.log
BASE=/home/USER/books
DL=$BASE/downloads
MANIFEST=/tmp/test_manifest.txt

head -3 $BASE/download_manifest.txt > $MANIFEST
mkdir -p $DL
cd $DL
: > $LOGFILE

download_one() {
  local file="$1"
  local url="$2"
  if [ -f "$file" ] && [ -s "$file" ]; then
    echo "SKIP $file" >> "$LOGFILE"
    return 0
  fi
  if wget -q -c -L -T 90 -t 3 -U "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" \
       -O "$file.tmp" "$url" 2>> "$LOGFILE"; then
    mv "$file.tmp" "$file"
    echo "OK $file" >> "$LOGFILE"
    return 0
  else
    rm -f "$file.tmp"
    echo "FAIL $file" >> "$LOGFILE"
    return 1
  fi
}
export -f download_one
export LOGFILE

awk -F'\t' '{print $1 "\t" $2}' "$MANIFEST" | \
  xargs -P "$WORKERS" -n 2 bash -c 'download_one "$0" "$1"'

echo "=== LOG ==="
cat "$LOGFILE"
echo "=== FILES ==="
ls -la $DL | grep -v "^total\|^d" | head
