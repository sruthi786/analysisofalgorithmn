import heapq
import tkinter as tk
from tkinter import ttk

# Huffman Node Class
class HuffmanNode:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

# Function to Build Huffman Tree
def build_huffman_tree(symbols):
    heap = [HuffmanNode(symbol, freq) for symbol, freq in symbols.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = HuffmanNode(None, left.frequency + right.frequency)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)

    return heap[0] if heap else None

# Function to Generate Huffman Codes
def generate_huffman_codes(node, code="", codes={}):
    if node:
        if node.symbol is not None:
            codes[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", codes)
        generate_huffman_codes(node.right, code + "1", codes)
    return codes

# GUI Interface
class HuffmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Greedy Huffman Coding")
        
        # Labels and Input
        ttk.Label(root, text="Enter Symbol & Frequency (comma separated):").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.input_entry = ttk.Entry(root, width=40)
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Buttons
        self.compute_button = ttk.Button(root, text="Compute Huffman Codes", command=self.compute_huffman)
        self.compute_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Output Area
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def compute_huffman(self):
        user_input = self.input_entry.get()
        try:
            symbols = dict(map(lambda x: (x.split(":")[0].strip(), int(x.split(":")[1].strip())), user_input.split(",")))
            root = build_huffman_tree(symbols)
            codes = generate_huffman_codes(root)
            
            output = "\n".join([f"{symbol}: {code}" for symbol, code in codes.items()])
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, output)
        except Exception:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Invalid Input! Use format: A:5, B:2, C:1")

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = HuffmanGUI(root)
    root.mainloop()