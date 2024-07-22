def hash_scrpt(txt):
    hv = 0
    pos = 0
    for let in txt:
        pos = (pos % 3) + 1
        hv = (hv + (pos * ord(let))) % 1000000
    return hv

# Generate candidate strings
import itertools
import string

def collision(min_length=3, max_length=10):
    chars = string.ascii_letters  # Using both lowercase and uppercase letters for more combinations
    hashes = {}

    for length in range(min_length, max_length + 1):
        for candidate in itertools.product(chars, repeat=length):
            candidate_str = ''.join(candidate)
            hv = hash_scrpt(candidate_str)
            if hv in hashes:
                return hashes[hv], candidate_str, hv
            hashes[hv] = candidate_str

    return None

# Find and print a collision
result = collision()
if result:
    str1, str2, hv = result
    print(f"Collision found:\nString 1: {str1}\nString 2: {str2}\nHash Value: {hv}")
else:
    print("No collision found within the given constraints.")