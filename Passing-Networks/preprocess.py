from statsbombpy import sb
from statsbomb_data import get_events
import pandas as pd

class Prep:
    
    def __init__(self, df):
        self.df = get_events()
    
    def get_passes(self, df):
        
        df['x'] = [i[0] for i in df['location'].values]
        df['y'] = [i[1] for i in df['location'].values]
        df['endX'] = [i[0] for i in df['pass_end_location'].values]
        df['endY'] = [i[1] for i in df['pass_end_location'].values]
        df['x'] = df['x'] * 
        df = df.drop(['location', 'pass_end_location'], axis =1)
        
        return df 
    