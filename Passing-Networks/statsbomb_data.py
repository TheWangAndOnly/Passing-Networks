from statsbombpy import sb
import pandas as pd

def get_competitions():
    pass

def get_matches(season_id=None, competition_id=None):
    return sb.matches(season_id, competition_id)

def get_events(match_id=None):
    return sb.events(match_id)
    
    
if __name__ == '__main__':
    pass