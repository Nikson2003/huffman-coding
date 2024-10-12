# Huffman Coding Compression

This project implements a simple Huffman coding algorithm for compressing and decompressing text files. Huffman coding is a popular method for lossless data compression, where frequently occurring characters are represented by shorter binary codes, thus reducing the overall file size.

## Features

- Compress text files into a binary format (`.bin`)
- Decompress binary files back to their original text format
- Error handling for empty input files

## Requirements

- Python 3.x

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Nikson2003/huffman-coding.git

2. Navigate into the project directory:

   ```bash
   cd huffman-coding

3. Ensure you have Python installed. You can check your Python version with:

    ```bash
   python --version

## Usage

1. Place the text file you want to compress in the project directory and update the path variable in main.py to point to your text file.

   ```bash
   path = "testing.txt"

2. Run the main.py script:

   ```bash
   python main.py

3. After running, the compressed file will be created in the same directory with a .bin extension. The decompressed text file will have _decompressed appended to the original filename.

## How It Works

1. Frequency Dictionary: The algorithm first calculates the frequency of each character in the input text.

2. Heap Creation: A min-heap is created based on the frequencies of the characters.

3. Huffman Tree Construction: Nodes are merged to create a binary tree, where each leaf node represents a character.

4. Code Generation: Binary codes are generated for each character based on their position in the tree.

5. Encoding: The input text is encoded into a binary string, padded to ensure its length is a multiple of 8 bits.

6. Compression: The padded binary string is converted into a byte array and written to a binary file.

7. Decompression: The binary file is read, decoded, and the original text is restored.
