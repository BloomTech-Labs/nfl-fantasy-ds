import pandas as pd


def check_and_add(data):
    winner = []
    if data.iloc[0]['week1Pred'] > data.iloc[1]['week1Pred']:
        winner.extend(['1','0'])
    elif data.iloc[1]['week1Pred'] > data.iloc[0]['week1Pred']:
        winner.extend(['0','1'])
    else:
        winner.extend(['0','0'])
    data['winner'] = winner
    return data
