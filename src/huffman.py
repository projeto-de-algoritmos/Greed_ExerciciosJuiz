import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = current_code
    build_huffman_codes(root.left, current_code + "0", huffman_codes)
    build_huffman_codes(root.right, current_code + "1", huffman_codes)

def huffman_encode(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1

    huffman_tree = build_huffman_tree(freq_dict)
    huffman_codes = {}
    build_huffman_codes(huffman_tree, "", huffman_codes)

    encoded_text = "".join(huffman_codes[char] for char in text)

    return encoded_text, huffman_codes

word = input("Digite uma palavra: ")
encoded_text, huffman_codes = huffman_encode(word)
print(f"Palavra codificada: '{word}': {encoded_text}")
print("Tabela de códigos de Huffman:")
for char, code in huffman_codes.items():
    print(f"'{char}': {code}")