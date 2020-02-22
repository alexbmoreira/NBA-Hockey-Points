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
        team.league = "NBA"
        team.name = page.find("h1", {"itemprop": "name"}).span.find_next().text
        #team.name = link[43:46]
        
        season_table = page.find("table", {"id": "games"})
        game_results = season_table.find_all("td", {"data-stat": "game_result"})
        overtimes = season_table.find_all("td", {"data-stat": "overtimes"})
        
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
        team.league = "NHL"
        team.name = page.find("h1", {"itemprop": "name"}).span.find_next().text
        #team.name = link[39:42]
        
        season_table = page.find("table", {"id": "games"})
        game_results = season_table.find_all("td", {"data-stat": "game_outcome"})
        overtimes = season_table.find_all("td", {"data-stat": "overtimes"})
        
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

def get_year():
    while True:
        try:
            year = input("Enter year in the format YYYY (1947-2020): ")
            if int(year) < 1947 or int(year) > 2020:
                print("Only dates from 1947 to the present year are valid.")
                continue

            return year
        except:
            print("Please enter a year in the format YYYY")
            continue

def get_nba_links(year):

    url = ""
    if int(year) < 1950:
        url = f"https://www.basketball-reference.com/leagues/BAA_{year}_ratings.html"
    else:
        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_ratings.html"

    request = requests.get(url)

    if request.status_code != 200:
        print("Connection Failed -> " + url)
        return []

    links = []

    page = request.text
    page = bs(page, "html.parser")

    table = page.find("table").find("tbody")
    
    for row in table.find_all("tr"):
        a = row.find('a', href=True)["href"]
        a = a[:-5] + "_games.html"
        links.append(f"https://www.basketball-reference.com{a}")

    return links

def get_nhl_links(year):

    url = f"https://www.hockey-reference.com/leagues/NHL_{year}_standings.html"

    request = requests.get(url)

    if request.status_code != 200:
        print("Connection Failed -> " + url)
        return []

    links = []

    page = request.text
    page = bs(page, "html.parser")

    table = page.find("table", {"id": "standings"}).find("tbody")

    for row in table.find_all("tr"):
        a = row.find('a', href=True)["href"]
        a = a[:-5] + "_games.html"
        links.append(f"https://www.hockey-reference.com{a}")

    return links

def write_file():
    print("Running...")
    nba_url = get_nba_links(year)
    nhl_url = get_nhl_links(year)
    # nba_codes = ["ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", \
    #              "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", \
    #              "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
    # nba_url = [f"https://www.basketball-reference.com/teams/{code}/{year}_games.html" for code in nba_codes]
    # nhl_codes = ["ANA", "ARI", "BOS", "BUF", "CGY", "CAR", "CHI", "COL", "CBJ", "DAL", \
    #              "DET", "EDM", "FLA", "LAK", "MIN", "MTL", "NSH", "NJD", "NYI", "NYR", \
    #              "OTT", "PHI", "PIT", "SJS", "STL", "TBL", "TOR", "VAN", "VEG", "WSH", "WPG"]
    # nhl_url = [f"https://www.hockey-reference.com/teams/{code}/{year}_games.html" for code in nhl_codes]

    file = open("hockey_points.csv", "w")
    points_csv_header = "rank,team name,gp,wins,losses,ot_losses,points,reg_wins,ppg,league\n"
    points_csv_string = ""

    teams = nhl_scrape(nhl_url)
    teams.extend(nba_scrape(nba_url))
    points_per(teams)
    teams = sort(teams)
    for team in teams:
        points_csv_string += str(team) + "\n"
    file.write(points_csv_header + points_csv_string)
    file.close()


if __name__ == "__main__":
    year = get_year()
    write_file(year)
