import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scrape

def graph_data():
    my_data = pd.read_csv("hockey_points.csv", index_col="rank")
    my_data = my_data.sort_values("rank", ascending=False)
    my_range = list(range(1, len(my_data.index) + 1))

    fig, ax = plt.subplots(figsize=(4.5,4.5))
    plt.hlines(y=my_range, xmin=0, xmax=my_data["points"], color='#007ACC', alpha=0.2, linewidth=1)
    plt.plot(my_data["points"], my_range, "o", markersize=3, color='#007ACC', alpha=0.6)

    ax.spines['left'].set_position(('data', 0.015))
    ax.set_xlabel("Points", fontsize=12, fontweight='black', color = '#333F4B')
    ax.set_ylabel("Team", fontsize=12, fontweight='black', color = '#333F4B')
    ax.set_title("NBA + NHL Combined Standings", fontsize=15, fontweight='black', color = '#333F4B')

    plt.yticks(my_range, my_data["team name"], fontsize=3)
    plt.xticks(list(range(0, 101, 5)), fontsize=5)

    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)

    plt.tight_layout()
    plt.savefig('standings.png', dpi=300, bbox_inches='tight')
    plt.show()

    
graph_data()