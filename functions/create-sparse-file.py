from pathlib import Path
import os

filename = "sparse"
sparse = Path(filename)
sparse.touch()
os.truncate(str(sparse), 10000)

# Write a single byte at offset xxx
with open(filename, 'wb+') as fp:
    os.lseek(fp.fileno(), 500202, os.SEEK_SET)
    fp.write(b'B')
    fp.write(b'\x97')
