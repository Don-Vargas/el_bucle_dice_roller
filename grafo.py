from graphviz import Digraph
from passing_days import *

# All days from your module
days = [
    #dia_1, dia_2, dia_3, dia_4, 
    dia_5,
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
    style = {
        "fillcolor": "white",
        "style": "filled",
        "fontsize": "36",  # bigger font for all normal nodes
        "width": "2",
        "height": "1.2"
    }

    if label in DUPLICATE_NODES:
        style.update({"fillcolor": "lightblue"})
    elif label in TERMINALS:
        style.update({"fillcolor": "lightcoral"})
    elif label in PRINCIPAL_NODES:
        style.update({
            "fillcolor": "lightyellow",
            "fontsize": "46",  # extra big for principal nodes
            "width": "2.5",
            "height": "2.0"
        })

    return style

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
            "size": "20,10",          # make the whole graph bigger
            "ratio": "auto",
            "splines": "compound",
            "nodesep": "1.5",         # more space between nodes
            "ranksep": "2.5",         # more space between ranks
            "fontsize": "36",         # global font size for graph labels
            "fontname": "Arial"
        },
        node_attr={
            "fontsize": "24",          # bigger node labels
            "width": "2",              # wider nodes
            "height": "1.2",           # taller nodes
            "shape": "doubleoctagon"
        },
        edge_attr={
            "fontsize": "20",          # bigger edge labels
            "penwidth": "3"
        }
    )
    
    seen_edges = set()
    seen_sequences = set()

    for path_index, path in enumerate(paths):
        path_tuple = tuple(path)
        if path_tuple in seen_sequences:
            continue
        seen_sequences.add(path_tuple)

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
