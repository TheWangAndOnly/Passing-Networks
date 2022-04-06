from statsbombpy import sb
from statsbomb_data import get_events
import pandas as pd

def choose_team(network, team):
    network = network[network['team'] == f"{team}"]
    return network

def get_passes(df):
    
    df['x'] = [i[0] for i in df['location'].values]
    df['y'] = [i[1] for i in df['location'].values]
    df['endX'] = [i[0] for i in df['pass_end_location'].values]
    df['endY'] = [i[1] for i in df['pass_end_location'].values]
    df['x'] = df['x'] * 1.05 #preferred size for most professional teams stadium (105m,68m)
    df['y'] = df['y'] * .68 
    df = df.drop(['location', 'pass_end_location'], axis =1)
    df = df[df['type'] == 'Pass']
    df = df.fillna('Suc')
    df = df[df['pass_outcome'] == 'Suc']
    
    return df 
    
def first_sub(df):
    first_sub = df['minute'].min()
    prenetwork = df[df['minute'].values <= first_sub]
    return prenetwork

def average_locations(prenetwork):
     
    avg = prenetwork.groupby('player').agg({'x':'mean', 'y':['mean', 'count']})
    avg.columns = ['x', 'y', 'count']
    
    return avg

def passes_between_players(prenetwork, avg):
    
    pass_between = prenetwork.groupby(['player', 'pass_recipient']).id.count().reset_index()
    pass_between = pass_between.rename({'id':'pass_count'}, axis='columns')
    network = pass_between.merge(avg, left_on='player', right_index=True)
    network = pass_between.merge(avg, left_on='pass_recipient', right_index=True)
    
    return network


if __name__ == '__main__':
    
    pass
    # 
    # events = get_events(match_id = )