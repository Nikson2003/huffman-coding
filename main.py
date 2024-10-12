from huffman import HuffmanCoding

path = "testing.txt"
h = HuffmanCoding(path)

try:
    output_path = h.compress()
    print(f"Compressed file path: {output_path}")

    decom_path = h.decompress(output_path)
    print(f"Decompressed file path: {decom_path}")
except ValueError as e:
    print(f"Error: {e}")
