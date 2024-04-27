from functools import partial

import networkx as nx
from matplotlib import animation

NODE_DEFAULT_COLOR = "#0064e1"


def update(ax, G, node_positions, title, frame):
    ax.clear()
    ax.axis("off")
    ax.set_title(title, horizontalalignment="right")

    background_nodes = nx.draw_networkx_nodes(
        G,
        nodelist=G.nodes(),
        pos=node_positions,
        node_color=NODE_DEFAULT_COLOR,
        ax=ax,
        alpha=0.5,
        edgecolors="k",
        linewidths=2,
    )

    graph_edges = nx.draw_networkx_edges(G, pos=node_positions, ax=ax)

    for node, color in frame:
        visited_nodes = nx.draw_networkx_nodes(
            G,
            nodelist=[node],
            pos=node_positions,
            node_color=color,
            ax=ax,
            edgecolors="k",
            linewidths=2,
        )


def animate_search(fig, ax, G, node_positions, title, explored_paths, interval=500):
    return animation.FuncAnimation(
        fig,
        partial(update, ax, G, node_positions, title),
        interval=interval,
        frames=explored_paths,
        repeat=False,
    )
