from tabulate import tabulate
nba_players = [['LeBron James',' Los Angeles Lakers'], ['Kevin Durant', 'Brooklyn Nets'], ['Stephen Curry', 'Golden State Warriors']]
print(tabulate(nba_players,headers =['Player','Team'],tablefmt = 'fancy_grid'))