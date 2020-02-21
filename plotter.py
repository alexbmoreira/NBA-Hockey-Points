import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import numpy as np
import pandas as pd
import scrape

def graph_data():
    my_data = pd.read_csv("hockey_points.csv", index_col="rank").sort_values("rank", ascending=False)
    my_range = list(range(1, len(my_data.index) + 1))

    fig, ax = plt.subplots(ncols=2, figsize=(9,4.5))
    ax_st = ax[1]
    ax_st.set_xlabel("Points", fontsize=12, fontweight='black', color = '#333F4B')
    ax_st.set_ylabel("Team", fontsize=12, fontweight='black', color = '#333F4B')
    ax_st.set_title("NBA + NHL Combined Standings", fontsize=15, fontweight='black', color = '#333F4B')
    ax_st.spines['top'].set_color('none')
    ax_st.spines['right'].set_color('none')
    ax_st.spines['left'].set_smart_bounds(True)
    ax_st.spines['bottom'].set_smart_bounds(True)
    ax_st.spines['left'].set_position(('data', 0.015))
    ax_st.plot(my_data["points"], my_range, "o", markersize=3, color='#007ACC', alpha=0.6)
    ax_st.hlines(y=my_range, xmin=0, xmax=my_data["points"], color='#007ACC', alpha=0.2, linewidth=1)
    ax_st.tick_params(axis="x", labelsize=5)

    plt.yticks(my_range, my_data["team name"], fontsize=3)
    plt.xticks(list(range(0, 101, 5)), fontsize=5)

    
    plt.tight_layout()
    plt.savefig('standings.png', dpi=300, bbox_inches='tight')
    plt.show()

    
graph_data()