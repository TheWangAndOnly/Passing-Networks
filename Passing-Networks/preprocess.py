from statsbombpy import sb
from statsbomb_data import get_events
import pandas as pd

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
    network = df[df['minute'].values <= first_sub]
    return network

def average_locations(network):
     
    avg = network.groupby('player').agg({'x':'mean', 'y':['mean', 'count']})
    avg.columns = ['x', 'y', 'count']
    
    return avg