Hockey Points in the NBA :ice_hockey: :basketball:
========================

How would the NBA look if points were given out the same way they were in the NHL?
----------------------------------------------------------------------------------

Teams are given 2 points for each win, 1 point for a loss in OT, and 0 points for a regulation loss.

This script will scrape data from [basketball-reference.com](https://www.basketball-reference.com) and [hockey-reference.com](https://www.hockey-reference.com) and show a combined 61-team seeding for both the NHL and NBA with points distributed as explained above.

How to run:
-----------

Using Python 3:
Run `> python scrape.py` and enter the date when prompted. This will write to a `.csv` called `hockey_points.csv`

This file is already sorted based on NHL points tie-breakers.

Once you have the `.csv` run `> python plotter.py` to output the lollipop plot of the standings

Why?
----
This was made to practice coding in Python, build a small web scraper, and take that data and do something fun with it, even if it is really simple.

Last Year's Standings:
----------------------
![2019 Standings](https://i.ibb.co/xjk6fLv/standings-points.png "NBA + NHL Combined 2019 Standings")

This Year's Standings by PPG (Probably not up to date):
-------------------------------------------------------
![2020 Standings](https://i.ibb.co/p1ZJKbq/standings-ppg.png "NBA + NHL Combined 2020 Standings")