import pandas as pd


def check_and_add(data):
    winner = []
    player1_score = data.iloc[0]['week-pred']
    player2_score = data.iloc[1]['week-pred']
    
    if player1_score > player2_score:
        winner.extend(['1','0'])
    elif player1_score < player2_score:
        winner.extend(['0','1'])
    else:
        winner.extend(['0','0'])

    data['winner'] = winner
    
    return data
