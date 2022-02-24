from statsbombpy import sb
import pandas as pd

def get_matches(season_id=None, competition_id=None):
    return sb.matches(season_id, competition_id)

def get_events(match_id=None):
    
    events = sb.events(match_id)
    events = events[['id','team','player','position','pass_recipient','minute',
                    'type', 'location', 'pass_end_location', 'pass_outcome',
                   ]]
    events = events[events['type'] == 'Pass']
    
    return events
