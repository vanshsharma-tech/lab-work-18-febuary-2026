# Compress a string using character counts.
def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    # Append the last character and its count
    compressed.append(s[-1] + str(count))

    return ''.join(compressed)

# Example usage
input_string = "aaabbcaaa"
compressed_string = compress_string(input_string)
print(f"Compressed string: {compressed_string}")
