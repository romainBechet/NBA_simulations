import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.colors import Normalize
from matplotlib import cm


def create_ranking(df: pd.DataFrame, conference) -> pd.DataFrame: 

    places = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    dic = dict((a, []) for a in places)

    for place in places: 
        dic[place] = dict((b, 0) for b in conferences[conference])

    for i in range(len(df)): 
        season = df.iloc[i]

        for team in conferences[conference]: 
            place = season[team]
            dic[place][team] += 1

    for el in dic: 
        for team in dic[el]: 
            dic[el][team] = np.round(dic[el][team] / len(df) *100,1)

    ranking = pd.DataFrame(dic)
    return ranking


def get_wins(df: pd.DataFrame, conference):
    wins = []
    for team in conferences[conference]: 
        result_team = df[team].mean()
        wins.append(int(np.round(result_team)))

    return wins


def plot_ranking(df: pd.DataFrame, conference): 

    wins = pd.DataFrame(df['Wins'])
    df = df.drop('Wins', axis = 1)

    vals = df.values 
    vals_without_zero = df.replace(0, "").values

    normal = Normalize(vals.min(), vals.max())

    if conference == 'western_conference': 
        color = cm.Reds(normal(vals))
    elif conference == 'eastern_conference': 
        color = cm.Blues(normal(vals))
    else: 
        print('Error')
        return 


    fig = plt.figure()
    plt.table(
        cellText= vals_without_zero, 
        cellLoc= 'center', 
        rowLabels= df.index, 
        colLabels= df.columns, 
        cellColours= color, 
        loc ='center',
    )

    plt.text(0.55, 0.97, f'{conference} estimated final ranking (in %)', ha = 'center', fontsize = 9)
    plt.axis('off')

    table = plt.table(
        cellText= wins.values, 
        loc = 'right', 
        cellLoc='center', 
        colWidths=[0.1], 
        colLabels='Wins',
    )

    table.auto_set_font_size(False)
    table.set_fontsize(8)

    plt.show()



df = pd.read_csv('data/results_rank.csv')

wins = pd.read_csv('data/results_wins.csv')

conferences = {
    'western_conference' : ['Dal','Den', 'GSW', 'Hou', 'LAL', 'LAC', 'Mem', 'Min', 'Nor',  'OKC', 'Pho', 'Por', 'Sac',  'SAS', 'Uta'],
    'eastern_conference' : ['Atl', 'Bos', 'Bkn', 'Cha', 'Chi', 'Cle', 'Det','Ind', 'Mia', 'Mil','NYK','Orl', 'Phi','Tor', 'Was']
}

for conference in conferences: 

    ranking = create_ranking(df, conference)
    wins_array = get_wins(wins, conference)

    ranking['Wins'] = wins_array
    ranking = ranking.sort_values(by='Wins', ascending = False)

    plot_ranking(ranking, conference)
