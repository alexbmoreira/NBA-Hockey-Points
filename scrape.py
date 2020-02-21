import requests
from bs4 import BeautifulSoup as bs
from team import Team
from operator import attrgetter

def nba_scrape(url):
    teams = []

    for link in url:
        request = requests.get(link)

        if request.status_code != 200:
            print("Connection Failed -> " + link)
            continue

        page = request.text
        page = bs(page, "html.parser")

        team = Team()
        team.name = page.find("h1", {"itemprop": "name"}).span.find_next().text
        #team.name = link[43:46]
        
        game_results = page.find_all("td", {"data-stat": "game_result"})
        overtimes = page.find_all("td", {"data-stat": "overtimes"})
        
        for i, (game_result, overtime) in enumerate(zip(game_results, overtimes)):
            if game_result.text != "":
                team.gp += 1
            
            if game_result.text == "L":
                if overtime.text != "":
                    team.points += 1
                    team.ot_losses += 1
                else:
                    team.losses += 1
            elif game_result.text == "W":
                team.points += 2
                team.wins += 1
                if overtime.text == "":
                    team.reg_wins += 1

        teams.append(team)

    return teams


def nhl_scrape(url):
    teams = []

    for link in url:
        request = requests.get(link)

        if request.status_code != 200:
            print("Connection Failed -> " + link)
            continue

        page = request.text
        page = bs(page, "html.parser")

        team = Team()
        team.name = page.find("h1", {"itemprop": "name"}).span.find_next().text
        #team.name = link[39:42]
        
        game_results = page.find_all("td", {"data-stat": "game_outcome"})
        overtimes = page.find_all("td", {"data-stat": "overtimes"})
        
        for i, (game_result, overtime) in enumerate(zip(game_results, overtimes)):
            if game_result.text != "":
                team.gp += 1
            
            if game_result.text == "L":
                if overtime.text != "":
                    team.points += 1
                    team.ot_losses += 1
                else:
                    team.losses += 1
            elif game_result.text == "W":
                team.points += 2
                team.wins += 1
                if overtime.text == "":
                    team.reg_wins += 1

        teams.append(team)

    return teams

# def nhl_scrape(url):
#     teams = []

#     request = requests.get(link)

#     if request.status_code != 200:
#         print("Connection Failed -> " + link)
#         continue

#     page = request.text
#     page = bs(page, "html.parser")
#     table = page.find("div", {"id": "all_stats"})
#     table = table.find("tbody")
#     rows = table.find_all("tr")

#     for row in rows:
#         team = Team()

#         team.name = row.find("td", {"data-stat": "team_name"}).text
#         team.gp = row.find("td", {"data-stat": "games"}).text
#         team.wins = row.find("td", {"data-stat": "wins"}).text
#         team.losses = row.find("td", {"data-stat": "losses"}).text
#         team.ot_losses = row.find("td", {"data-stat": "losses_ot"}).text
#         team.points = row.find("td", {"data-stat": "points"}).text
#         team.reg_wins = 0

#     return teams

def points_per(teams):
    for team in teams:
        team.points_per_game()

def sort(teams):
    s = sorted(teams, key = attrgetter("reg_wins"), reverse = True)
    s = sorted(s, key = attrgetter("gp"))
    s = sorted(s, key = attrgetter("points"), reverse = True)
    for i, team in enumerate(s):
        team.standing = i + 1

    return s

if __name__ == "__main__":
    nba_codes = ["ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", \
                 "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", \
                 "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
    nba_url = [f"https://www.basketball-reference.com/teams/{code}/2020_games.html" for code in nba_codes]
    nhl_codes = ["ANA", "ARI", "BOS", "BUF", "CGY", "CAR", "CHI", "COL", "CBJ", "DAL", \
                 "DET", "EDM", "FLA", "LAK", "MIN", "MTL", "NSH", "NJD", "NYI", "NYR", \
                 "OTT", "PHI", "PIT", "SJS", "STL", "TBL", "TOR", "VAN", "VEG", "WSH", "WPG"]
    nhl_url = [f"https://www.hockey-reference.com/teams/{code}/2020_games.html" for code in nhl_codes]
    #nhl_url = "https://www.hockey-reference.com/leagues/NHL_2020.html"

    file = open("hockey_points.csv", "w")
    points_csv_header = "rank,team name,gp,wins,losses,ot_losses,points,reg_wins,ppg\n"
    points_csv_string = ""

    teams = nhl_scrape(nhl_url)
    teams.extend(nba_scrape(nba_url))
    points_per(teams)
    teams = sort(teams)
    for team in teams:
        points_csv_string += str(team) + "\n"
    file.write(points_csv_header + points_csv_string)
    file.close()
