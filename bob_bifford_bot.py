import bs4, requests

def getFumbblTournamentNames(fumbblUrl):
    res = requests.get(fumbblUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    ## TODO: build iterator to go over all returned game names. Store the ones we want in a list
    for x in range (0, 50):
        try:
            elems = soup.select('body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child('') > a')
            return elems[0].text
        except IndexError:
            print('no game with that id')

    ## TODO: take the list and then filter out ones that do not match league name

current_tournament_list = getFumbblTournamentNames('https://fumbbl.com/p/games')
print('The current Underground tournaments are: ' + current_tournament_list)