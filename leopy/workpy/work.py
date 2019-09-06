import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import os

def plot_curve():
    '''plot curve read from registers.'''
    data = pd.read_excel('Plot.xlsx', sheet_name="Sheet1",header=None)
    iq = data[2]
    plt.plot(iq)
    plt.show()

def open_app():
    os.startfile(r'C:\Octave\Octave-4.2.1\bin\octave-gui.exe')
    os.startfile(r'C:\Program Files (x86)\Microsoft Office\Office15\OUTLOOK.EXE')
    os.startfile(r'C:\Users\leozhang\AppData\Local\GitHubDesktop\GitHubDesktop.exe')
    os.startfile(r'C:\Users\leozhang\AppData\Local\Apps\Evernote\Evernote\Evernote.exe')