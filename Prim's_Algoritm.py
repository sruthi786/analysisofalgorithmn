import tkinter as tk
from tkinter import ttk, messagebox
import heapq

# Prim's Algorithm Implementation
def prim(graph, start):
    mst = []
    visited = set()
    pq = [(0, start, None)]  # (weight, node, parent)
    
    while pq:
        weight, node, parent = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if parent is not None:
            mst.append((parent, node, weight))
        
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor, node))

    return mst

# GUI Class
class PrimGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Prim's Algorithm - GUI")

        # Labels and Input Fields
        ttk.Label(root, text="Enter Graph Edges (Format: A,B,Weight)").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.edge_entry = ttk.Entry(root, width=40)
        self.edge_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(root, text="Enter Start Node:").grid(row=2, column=0, padx=10, pady=5)
        self.start_entry = ttk.Entry(root, width=10)
        self.start_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        self.compute_button = ttk.Button(root, text="Compute MST", command=self.compute_prim)
        self.compute_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Output Area
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def compute_prim(self):
        try:
            edges = [tuple(entry.split(",")) for entry in self.edge_entry.get().split(";")]
            graph = {}
            
            for src, dest, weight in edges:
                weight = int(weight.strip())
                if src not in graph:
                    graph[src] = []
                if dest not in graph:
                    graph[dest] = []
                graph[src].append((dest, weight))
                graph[dest].append((src, weight))  # Assuming an undirected graph

            start_node = self.start_entry.get().strip()
            if start_node not in graph:
                messagebox.showerror("Error", "Start node is not in the graph!")
                return

            mst_edges = prim(graph, start_node)
            output = "\n".join([f"{u} - {v}: {w}" for u, v, w in mst_edges])

            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, output)

        except Exception:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Invalid Input! Use format: A,B,5; C,D,3")

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = PrimGUI(root)
    root.mainloop()