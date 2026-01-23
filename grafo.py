from graphviz import Digraph
from passing_days import *

# All days from your module
days = [
    dia_1, dia_2, dia_3, dia_4, dia_5,
    dia_6, dia_7, dia_8, dia_9, dia_10
]

# Terminal nodes that end a path
TERMINALS = ("dormir", "muerto")

def split_day_general(day, terminal=TERMINALS):
    """
    Split a sequence into multiple paths at repeated nodes or terminal nodes.
    
    - Each repeated node starts a new path segment.
    - Paths stop at terminal nodes.
    """
    if not day:
        return []

    paths = []
    current = []

    for node in day:
        if node in current:
            # Node repeats, start a new path from this node
            paths.append(current.copy())
            current = [node]
        else:
            current.append(node)

        if node in terminal:
            paths.append(current.copy())
            break

    if current and current[-1] not in terminal:
        paths.append(current.copy())

    return paths

DUPLICATE_NODES = {"1", "75"}
TERMINALS = {"24", "dormir", "muerto"}
PRINCIPAL_NODES = {"100", "150", "200", "300"}

def get_node_style(label):
    """Return Graphviz style for a node based on its label."""
    if label in DUPLICATE_NODES:
        return {"fillcolor": "lightblue", "style": "filled", "fontsize": "12"}
    elif label in TERMINALS:
        return {"fillcolor": "lightcoral", "style": "filled", "fontsize": "12"}
    elif label in PRINCIPAL_NODES:
        return {"fillcolor": "lightyellow", "style": "filled", "fontsize": "36", "width": "1.5", "height": "1.5"}
    else:
        return {"fillcolor": "white", "style": "filled", "fontsize": "12"}

def make_internal_name(node, path_index):
    """Generate a unique internal node name for duplicable or terminal nodes."""
    if node in DUPLICATE_NODES or node in TERMINALS or node == "24":
        return f"{node}_{path_index}"
    return node

def add_edges(graph, path_copy, seen_edges):
    """Add edges and nodes to the graph using NODE_INFO for labels."""
    for (a_name, a_label), (b_name, b_label) in zip(path_copy, path_copy[1:]):
        edge = (a_name, b_name)
        if edge not in seen_edges:
            a_info = NODE_INFO.get(a_label, {"label": a_label, "clue": ""})
            b_info = NODE_INFO.get(b_label, {"label": b_label, "clue": ""})

            # Combina label y clue para que se vea dentro del nodo
            a_label_text = f"{a_info['label']}\n[{a_info.get('clue','')}]"
            b_label_text = f"{b_info['label']}\n[{b_info.get('clue','')}]"

            graph.node(a_name, label=a_label_text, **get_node_style(a_label))
            graph.node(b_name, label=b_label_text, **get_node_style(b_label))
            
            # Mantén tooltip si quieres pasar el ratón (solo SVG lo soporta)
            graph.edge(a_name, b_name, tooltip=a_info.get("clue", ""))
            
            seen_edges.add(edge)

def build_graph(paths):
    """Build a directed graph from a list of paths, showing each unique sequence only once."""
    graph = Digraph(
        "paths",
        format="svg",
        graph_attr={
            "size": "10,5",     # ancho 20in, alto 10in, "!" fuerza exacto tamaño
            "ratio": "auto",      # deja que Graphviz ajuste la relación de aspecto
            "splines": "compound",   # opcional, para líneas más claras
            "nodesep": "1.0",     # separación entre nodos
            "ranksep": "1.0"      # separación entre niveles
        }
    )
    
    seen_edges = set()
    seen_sequences = set()

    for path_index, path in enumerate(paths):
        # Convert path to tuple for hashing
        path_tuple = tuple(path)
        if path_tuple in seen_sequences:
            continue  # skip duplicate sequences
        seen_sequences.add(path_tuple)

        # Generate internal names
        path_copy = [(make_internal_name(node, path_index), node) for node in path]
        add_edges(graph, path_copy, seen_edges)

    return graph

# --- Main script ---

all_paths = []

for i, day in enumerate(days, start=1):
    day_paths = split_day_general(day)
    all_paths.extend(day_paths)

# Build and render the graph
graph = build_graph(all_paths)
graph.render("paths_graph", view=True)
