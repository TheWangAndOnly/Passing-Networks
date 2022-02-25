from statsbombpy import sb
from statsbomb_data import get_events
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from mplsoccer import Pitch, FontManager
import warnings
import pandas as pd
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

def choose_team(network, team):
    network = network[network['team'] == f"{team}"]
    return network 


if __name__ == '__main__':
    pass