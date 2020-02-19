import matplotlib.pyplot as plt
import pandas as pd
import scrape

def get_data():
    my_data = pd.read_csv("hockey_points.csv", delimiter=",")

    #print(my_data)
    #print(my_data["team name"])
    #print(my_data.loc["0":, "points"])

    print(my_data["points"]["93"])

    #fig = plt.figure()
    #axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    #axes.plot(my_data["points"], my_data["team_name"])
    plt.show()

get_data()