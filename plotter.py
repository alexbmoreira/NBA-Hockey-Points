import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scrape

def get_data_pd():
    my_data = pd.read_csv("hockey_points.csv", index_col="rank")
    standings = my_data.loc["1":, ["points", "team name"]]

    my_range = list(range(1, len(my_data.index) + 1))

    fig, ax = plt.subplots(figsize=(5,5))
    plt.hlines(y=my_range, xmin=0, xmax=my_data["points"], color='#007ACC', alpha=0.2, linewidth=1)
    plt.plot(my_data["points"], my_range, "o", markersize=3, color='#007ACC', alpha=0.6)

    ax.spines['left'].set_position(('data', 0.015))
    ax.set_xlabel("Points", fontsize=15, fontweight='black', color = '#333F4B')
    ax.set_ylabel("Team", fontsize=15, fontweight='black', color = '#333F4B')
    ax.set_title("NBA + NHL Combined Standings")

    plt.yticks(my_range, my_data["team name"], fontsize=3)
    plt.xticks(list(range(0, 101, 5)), fontsize=3)

    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)

    #print(my_data)
    #print(standings)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('standings.png', dpi=300, bbox_inches='tight')
    plt.show()

def get_data_np():
    my_data = np.genfromtxt("hockey_points.csv", delimiter=",", skip_header=1,\
                            dtype=[('rank', '<i4'), ('team', '<U3'), ('gp', '<i4'), \
                            ('w', '<i4'), ('l', '<i4'), ('otl', '<i4'), ('p', '<i4'), ('rw', '<i4'), ])


    y = my_data["p"]
    x = my_data["team"]

    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    axes.barh(x, y)

    axes.set_xlabel("Points")
    axes.set_ylabel("Team")
    axes.set_title("NBA + NHL Combined Points Standings")

    plt.hlines(y=y, xmin=0, xmax=61, color='#007acc', alpha=0.2, linewidth=5)
    plt.gca().invert_yaxis()
    plt.show()
    #print(my_data)

#get_data_np()
get_data_pd()