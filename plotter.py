import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scrape

def get_data():
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

get_data()