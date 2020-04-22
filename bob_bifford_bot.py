import bs4, requests

def getFumbblTournamentNames(fumbblUrl):
    res = requests.get(fumbblUrl)
    res.raise_for_status()

    current_games = []

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    ## TODO: maybe dynamically check the # of current games? (currently checking a static 100)
    for x in range (0, 100):
        try:
            css_selector = 'body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child({}) > a'
            elems = soup.select(css_selector.format(x))
            if elems[0].text != IndexError:
                current_games.append(elems[0].text)
             ##   print (elems[0].text)
        except IndexError:
         ##   print('no game with that id')
            continue
    return current_games

    ## TODO: take the list and then filter out ones that do not match league name
def leagueFilter(current_games):


current_tournament_list = getFumbblTournamentNames('https://fumbbl.com/p/games')
## print('The current Underground tournaments are: ' + current_tournament_list)