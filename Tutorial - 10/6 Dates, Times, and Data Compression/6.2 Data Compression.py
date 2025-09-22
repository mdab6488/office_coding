# Python provides several modules for data compression, which is valuable for web applications that need to reduce bandwidth usage, optimize storage, or work with compressed file formats.

import zlib
import gzip
import bz2
import lzma

# Compress data for efficient storage or transmission
original_data = b"This is some sample data that will be compressed. " * 100
print(f"Original size: {len(original_data)} bytes")

# zlib compression
zlib_compressed = zlib.compress(original_data)
print(f"zlib compressed size: {len(zlib_compressed)} bytes")

# Decompress data
zlib_decompressed = zlib.decompress(zlib_compressed)
print(f"Decompressed equals original: {original_data == zlib_decompressed}")

# Working with gzip files (common for web)
with gzip.open('example.txt.gz', 'wb') as f:
    f.write(original_data)

# Read gzip files
with gzip.open('example.txt.gz', 'rb') as f:
    decompressed_data = f.read()

print(f"GZIP file content length: {len(decompressed_data)} bytes")

# Calculate checksum for data integrity verification
checksum = zlib.crc32(original_data)
print(f"Data checksum: {checksum}")

# These compression capabilities are particularly useful for web applications that need to optimize data transfer between servers and clients or reduce storage requirements for user-generated content 