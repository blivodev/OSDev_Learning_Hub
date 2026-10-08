#!/bin/bash
# Download the book library to cPanel. Run on server, resumable.
# Usage: bash download_books.sh <workers> <logfile>
set -u
WORKERS="${1:-12}"
LOGFILE="${2:-download.log}"
BASE="/home/USER/books"
DL="$BASE/downloads"
MANIFEST="$BASE/download_manifest.txt"

mkdir -p "$DL"
cd "$DL"
: > "$LOGFILE"

download_one() {
  local file="$1"
  local url="$2"
  if [ -f "$file" ] && [ -s "$file" ]; then
    echo "SKIP $file" >> "$LOGFILE"
    return 0
  fi
  if wget -q -c -L -T 90 -t 5 -U "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" \
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

DOTOTAL=$(wc -l < "$MANIFEST")
echo "Starting download of $DOTOTAL files with $WORKERS workers"

# Read manifest FILE<TAB>URL, call download_one for each, parallel with xargs
awk -F'\t' '{print $1 "\t" $2}' "$MANIFEST" | \
  xargs -P "$WORKERS" -n 2 bash -c 'download_one "$0" "$1"'

OKCOUNT=$(grep -c "^OK " "$LOGFILE" || true)
SKIPCOUNT=$(grep -c "^SKIP " "$LOGFILE" || true)
FAILCOUNT=$(grep -c "^FAIL " "$LOGFILE" || true)
echo "DONE ok=$OKCOUNT skip=$SKIPCOUNT fail=$FAILCOUNT total=$DOTOTAL"
echo "DONE ok=$OKCOUNT skip=$SKIPCOUNT fail=$FAILCOUNT total=$DOTOTAL" >> "$LOGFILE"
