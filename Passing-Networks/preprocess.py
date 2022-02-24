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
    
    
    return df 
    
