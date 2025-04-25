import tkinter as tk
from tkinter import ttk, messagebox

# Disjoint Set Class for Kruskal's Algorithm
class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, node):
        self.parent[node] = node
        self.rank[node] = 0

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

# Kruskal's Algorithm Implementation
def kruskal(graph):
    ds = DisjointSet()
    mst = []
    
    for node in graph.keys():
        ds.make_set(node)

    edges = sorted([(weight, src, dest) for src in graph for dest, weight in graph[src]], key=lambda x: x[0])

    for weight, src, dest in edges:
        if ds.find(src) != ds.find(dest):
            ds.union(src, dest)
            mst.append((src, dest, weight))
    
    return mst

# GUI Class for Kruskal's Algorithm
class KruskalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kruskal's Algorithm - GUI")

        # Labels and Input Fields
        ttk.Label(root, text="Enter Graph Edges (Format: A,B,Weight)").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.edge_entry = ttk.Entry(root, width=40)
        self.edge_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Buttons
        self.compute_button = ttk.Button(root, text="Compute MST", command=self.compute_kruskal)
        self.compute_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Output Area
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def compute_kruskal(self):
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
                graph[dest].append((src, weight))  # Undirected Graph

            mst_edges = kruskal(graph)
            output = "\n".join([f"{u} - {v}: {w}" for u, v, w in mst_edges])

            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, output)

        except Exception:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Invalid Input! Use format: A,B,5; C,D,3")

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = KruskalGUI(root)
    root.mainloop()