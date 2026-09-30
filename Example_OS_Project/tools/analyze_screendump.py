import sys
fn = sys.argv[1]
with open(fn,'rb') as f:
    data = f.read()
if data[:2] != b'P6':
    print("not P6"); sys.exit(1)
# dimensions on second line
second = data.split(b'\n', 3)
dims = second[1].split()
w, h = int(dims[0]), int(dims[1])
idx = data.index(b'255\n') + 4
px = data[idx:]
print("PPM %dx%d, %d pixel-bytes" % (w,h,len(px)))
# Text mode: 80 cols x 25 rows, each glyph ~8x16 -> 720x400. Character cell 9 wide (8px + blank) is common.
cell_w = 9
cell_h = 16
# Build a per-cell brightness grid and reconstruct which cells are lit.
# White text: r,g,b > 200. Detect lit cells.
lit = set()
for y in range(h):
    row = y // 16
    for x in range(w):
        col = x // 9
        o = (y*w+x)*3
        if px[o] > 180 and px[o+1] > 180 and px[o+2] > 180:
            lit.add((row, col))
# Determine occupied cell columns in top rows
grid = {}
for (r,c) in lit:
    grid.setdefault(r, set()).add(c)
nrows = max(grid) + 1 if grid else 0
ncols = max((max(v) for v in grid.values())) + 1 if grid else 0
print("Total lit VGA cells:", len(lit), " spanning %d rows x %d cols" % (nrows, ncols))
# Print an ASCII rendering of the top rows so we can ID the text
for r in sorted(grid):
    if r > 10: break
    line = ''.join('#' if c in grid[r] else '.' for c in range(min(45, ncols+1)))
    print("row %2d: %s" % (r, line))
