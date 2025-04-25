import tkinter as tk
from tkinter import ttk, messagebox
import heapq

# Dijkstra's Algorithm Implementation
def dijkstra(graph, start):
    pq = [(0, start)]  # Priority queue (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# GUI Class
class DijkstraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dijkstra's Algorithm - GUI")

        # Labels and Input Fields
        ttk.Label(root, text="Enter Graph Edges (Format: A,B,Weight)").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.edge_entry = ttk.Entry(root, width=40)
        self.edge_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(root, text="Enter Start Node:").grid(row=2, column=0, padx=10, pady=5)
        self.start_entry = ttk.Entry(root, width=10)
        self.start_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        self.compute_button = ttk.Button(root, text="Compute Shortest Paths", command=self.compute_dijkstra)
        self.compute_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Output Area
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def compute_dijkstra(self):
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

            distances = dijkstra(graph, start_node)
            output = "\n".join([f"Shortest path to {node}: {dist}" for node, dist in distances.items()])

            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, output)

        except Exception:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Invalid Input! Use format: A,B,5; C,D,3")

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = DijkstraGUI(root)
    root.mainloop()