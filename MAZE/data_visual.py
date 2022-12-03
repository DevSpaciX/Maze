import matplotlib.pyplot as plt


def visual_maze(way: list) -> plt:
    y_line = []
    x_line = []
    for i in way:
        x_line.append(i[1])
        y_line.append(i[0])

    plt.plot(
        x_line,
        y_line,
        color="red",
        linestyle="dashed",
        linewidth=4,
        marker="o",
        markersize=10,
        drawstyle="steps-post",
    )

    plt.text(x_line[0], y_line[0], "  Start", rotation=12, fontsize=20)
    plt.text(x_line[-1], y_line[-1], "  Finish", rotation=12, fontsize=20)
    plt.ylim(11, 0)
    plt.xlim(0, 10)

    plt.grid()
    return plt.show()
