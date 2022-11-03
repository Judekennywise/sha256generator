# Python program to find SHA256 hash string of a file
import hashlib
 
nftjson_file = input(r"Enter the file path: ")
sha256_hash = hashlib.sha256()
with open(nftjson_file,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    print(sha256_hash.hexdigest())
