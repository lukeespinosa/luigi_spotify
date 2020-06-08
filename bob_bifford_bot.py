import bs4, requests, re

## grab all 'tournament names' and their css selector - while we are here, grab home/away team info and store in a list
def getFumbblTournamentNames(fumbblUrl):
    res = requests.get(fumbblUrl)
    res.raise_for_status()

    current_games = []

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    ## TODO: maybe dynamically check the # of current games? (currently checking a static 100)
    for x in range (0, 100):
        try:
            league_name_selector = 'body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child({}) > a'
            home_team_selector = 'body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child({}) > div.home > div.team > a'
            home_race_selector = 'body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child({}) > div.home > div.race'
            away_team_selector = 'body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child({}) > div.away > div.team > a'
            away_race_selector = 'body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child({}) > div.away > div.race'
            elems = soup.select(league_name_selector.format(x))
            if elems[0].text != IndexError:
                home_elems = soup.select(home_team_selector.format(x+1))
                home_race_elems = soup.select(home_race_selector.format(x+1))
                away_elems = soup.select(away_team_selector.format(x+1))
                away_race_elems = soup.select(away_race_selector.format(x+1))
                current_games.append(str(elems[0].text) + ' ----- '
                                     + ' home team: ' + str(home_elems[0].text)
                                     + ' home coach info: ' + str(home_race_elems[0].text)
                                     + ' away team: ' + str(away_elems[0].text)
                                     + ' away coach info: ' + str(away_race_elems[0].text))
             ##   print (elems[0].text)
        except IndexError:
         ##   print('no game with that id')
            continue
    return current_games

    ## TODO: take the list and then filter out ones that do not match league name
def leagueFilter(current_games):

    print("the original list is :" + str(current_games))

    subs = 'Veteran Bowl'

    res = {x for x in current_games if re.search(subs, x)}

    print("after filtering for game name :" + str(res))

## def getMatchDetails():


current_tournament_list = leagueFilter(getFumbblTournamentNames('https://fumbbl.com/p/games'))
## print('The current Underground tournaments are: ' + current_tournament_list)


## CSS Selector notes TODO: remove once done, can add to readme notes

## League name:
# body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child(6) > a

## Left team name selector:
# body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child(7) > div.home > div.team > a

## Right team name selector:
# body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child(7) > div.away > div.team > a