import bs4, requests

def getFumbblTournamentNames(fumbblUrl):
    res = requests.get(fumbblUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('body > div.contentwrapper > div.pagecontent > div > div.gamescontent > div:nth-child(25) > a')
    return elems[0].text


current_tournament_list = getFumbblTournamentNames('https://fumbbl.com/p/games')
print('The current Underground tournaments are: ' + current_tournament_list)