from functools import partial

import matplotlib.animation as animation
import networkx as nx

NODE_DEFAULT_COLOR = "#0064e1"


def draw_path_edges(ax, G, node_positions, path):
    if len(path) == 1:
        return

    return nx.draw_networkx_edges(
        G,
        edgelist=[(a, b) for a, b in zip(path[:-1], path[1:])],
        pos=node_positions,
        edge_color="red",
        width=1.5,
        ax=ax,
    )


def update(ax, G, node_positions, title, frame):
    ax.clear()
    ax.axis("off")
    ax.set_title(title)
    background_nodes = nx.draw_networkx_nodes(
        G, nodelist=G.nodes(), pos=node_positions, node_color=NODE_DEFAULT_COLOR, ax=ax,
    )

    graph_edges = nx.draw_networkx_edges(G, pos=node_positions, ax=ax)

    if len(frame) > 1:
        path_edges = nx.draw_networkx_edges(
            G,
            edgelist=[(a, b) for a, b in zip(frame[:-1], frame[1:])],
            pos=node_positions,
            edge_color="red",
            width=1.5,
            ax=ax,
        )

    visited_nodes = nx.draw_networkx_nodes(
        G, nodelist=frame, pos=node_positions, node_color="red", ax=ax
    )

    nodes_labels = nx.draw_networkx_labels(
        G, pos=node_positions, labels={k: k for k in G.nodes}, ax=ax
    )


def animate_search(fig, ax, G, node_positions, title, explored_paths, interval=500):
    return animation.FuncAnimation(
        fig,
        partial(update, ax, G, node_positions, title),
        interval=interval,
        frames=explored_paths,
        repeat=False,
    )


# def draw_graph(ax, G, node_attrs, edge_labels=False):
#     nx.draw(G,
#             ax=ax,
#             pos=node_attrs["positions"],
#             with_labels=True,
#             node_size=500,
#             nodelist=list(node_attrs["colors"].keys()),
#             node_color=list(node_attrs["colors"].values()),
#             )

#     if edge_labels:
#         nx.draw_networkx_edge_labels(
#             G,
#             ax=ax,
#             pos=node_attrs["positions"],
#             edge_labels={edge: G.edges[edge]["weight"] for edge in G.edges},
#             font_size=15,
#             font_color="red",
#             )
