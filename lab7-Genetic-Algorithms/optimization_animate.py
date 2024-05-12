from functools import partial
from itertools import count

import matplotlib.animation as animation
from matplotlib import colormaps


def update(ax, f_xyz, title, frame):
    ax.clear()
    ax.set_title(
        title + "\nGeneration: " + str(next(generation)-1),
        horizontalalignment="right"
        )

    # background plot
    x, y, z = f_xyz
    ax.contour(x, y, z, levels=20, cmap=colormaps["gnuplot"])
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # update population
    ax.plot(frame[:, 0], frame[:, 1], "kx", linestyle="")


def animate_search(fig, ax, title, f_xyz, populations, interval=500):
    global generation
    generation = count()
    return animation.FuncAnimation(
        fig,
        partial(update, ax, f_xyz, title),
        interval=interval,
        frames=populations,
        repeat=False,
    )
