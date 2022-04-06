from statsbombpy import sb
from statsbomb_data import get_events
from preprocess import get_passes, first_sub, average_locations, passes_between_players
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from mplsoccer import Pitch, FontManager
import warnings
import pandas as pd
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

# NEED TO CHOOSE THE TEAM BEFORE PREPROCESSING ALL THE DATA. SHOULD BE EASIER LIKE THAT.

def plot(network):
    
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
    fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
    fig.set_facecolor("#22312b")
    # pass_lines = pitch.lines(pass_between.x_x, .pass_between.y_x, 
    #                         pass_between.x_y, .pass_between.y_y, 
    #                         #lw=passes_between.width,
    #                         color=color, zorder=1, ax=ax)

    # nodes = pitch.scatter(avg_locations.x, .avg_locations.y, s=300, 
    #                     color='purple', linewidth = 1.5, 
    #                     alpha = 1, zorder=1, ax=ax)

# MIN_TRANSPARENCY = 0.3
# color = np.array(to_rgba('white'))
# color = np.tile(color, (len(pass_between), 1))
# c_transparency = pass_between.pass_count / pass_between.pass_count.max()
# c_transparency = (c_transparency * (1 - MIN_TRANSPARENCY)) + MIN_TRANSPARENCY
# color[:, 3] = c_transparency

if __name__ == '__main__':
    pass