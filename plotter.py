import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import numpy as np
import pandas as pd
import scipy.stats as stats
import scrape

def graph_data():
    my_data = pd.read_csv("hockey_points.csv", index_col="rank").sort_values("rank", ascending=False)
    ppg_data = my_data.sort_values("ppg", ascending=True)
    nhl_ppg = ppg_data["league"] == "NHL"
    nba_ppg = ppg_data["league"] == "NBA"
    my_range = list(range(1, len(my_data.index) + 1))

    fig, ((ax_st, ax_ppg), (std_nba, std_nhl)) = plt.subplots(nrows=2, ncols=2, figsize=(9,7.5), gridspec_kw={'height_ratios': [3, 1]})



    axes_st(ax_st, my_data, my_range)

    axes_ppg(ax_ppg, ppg_data, my_range)

    plt.tight_layout()
    plt.savefig('standings.png', dpi=300, bbox_inches='tight')
    plt.show()

def axes_ppg(axes, data, my_range):
    axes.set_xlabel("Points per Game", fontsize=9, fontweight='black', color = '#333F4B')
    axes.set_ylabel("Team", fontsize=9, fontweight='black', color = '#333F4B')
    axes.set_title("Sorted by Points per Game", fontsize=11, fontweight='black', color = '#333F4B')
    axes.spines['top'].set_color('none')
    axes.spines['right'].set_color('none')
    axes.spines['left'].set_smart_bounds(True)
    axes.spines['bottom'].set_smart_bounds(True)
    axes.spines['left'].set_position(('data', 0.015))
    axes.plot(data["ppg"], my_range, "o", markersize=3, color='#007ACC', alpha=0.6)
    axes.hlines(y=my_range, xmin=0, xmax=data["ppg"], color='#007ACC', alpha=0.2, linewidth=1)
    axes.tick_params(axis="x", labelsize=5)
    plt.sca(axes)
    plt.yticks(my_range, data["team name"], fontsize=3)
    plt.xticks(list(np.linspace(0,1.75,20)), fontsize=5, rotation=45)

def axes_st(axes, data, my_range):
    axes.set_xlabel("Points", fontsize=9, fontweight='black', color = '#333F4B')
    axes.set_ylabel("Team", fontsize=9, fontweight='black', color = '#333F4B')
    axes.set_title("Sorted by Points", fontsize=11, fontweight='black', color = '#333F4B')
    axes.spines['top'].set_color('none')
    axes.spines['right'].set_color('none')
    axes.spines['left'].set_smart_bounds(True)
    axes.spines['bottom'].set_smart_bounds(True)
    axes.spines['left'].set_position(('data', 0.015))
    axes.plot(data["points"], my_range, "o", markersize=3, color='#007ACC', alpha=0.6)
    axes.hlines(y=my_range, xmin=0, xmax=data["points"], color='#007ACC', alpha=0.2, linewidth=1)
    axes.tick_params(axis="x", labelsize=5)
    plt.sca(axes)
    plt.yticks(my_range, data["team name"], fontsize=3)
    plt.xticks(list(range(0, 101, 5)), fontsize=5)
    
graph_data()