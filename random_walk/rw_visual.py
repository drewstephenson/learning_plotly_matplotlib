import matplotlib.pyplot as plt
from random_walk import RandomWalk


# This is just a program that executes RandomWalk until the user decides to stop
# Start a random walk, and plot the points

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('Solarize_Light2')
    fig, ax = plt.subplots(figsize=(6, 4), dpi=128)  # figsize resizes the window, dpi increases resolution
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap='Blues', edgecolors='none', s=1)  # no outline

    # Make starting and end points stand out
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    break

    # Ask to stop
    # keep_running = input("Make another walk? (y/n): ")
    # if keep_running == 'n':
        # break
