'intensity_before profile'

from statistics import mode
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import easygui
#pip install --upgrade easygui
import csv
import os
from matplotlib.offsetbox import AnchoredText

#############################

def samples_name(path_list):
    
    ''' Extracts the name/code of the sample from the file's name'''
    
    samples_name = []
    
    for _ in range(len(file_path_before)):
        selected_file = os.path.basename(os.path.normpath(file_path_before[_]))
        file_name     = selected_file[5:21]
        samples_name.append(file_name)
        
    return samples_name

def recentre(dist):
    z = []
    for i in dist:
        z.append(i-(max(dist)/2))

    return z

def get_raw_data(type, percentage):

    if type == 'force' | type == 1:   # raw data reletive to confocal force experiments
        if percentage == 5:
            dye_after = r"C:\Users\drb18182\Desktop\Docs\Data\confocal\MGG-165 [GPSomes, 5% % 95%, Gentle Hydation_v2, Lacc Nanoreactors\[IntProf] txt data\[IntProf] [FORCE] MGG165e_ 5 _Force+AR+1h_ABSOL.txt"
        else percentage == 95:
            dye_after = r"C:\Users\drb18182\Desktop\Docs\Data\confocal\MGG-165 [GPSomes, 5% % 95%, Gentle Hydation_v2, Lacc Nanoreactors\[IntProf] txt data\[IntProf] [FORCE] MGG165e_ 95 _Force+AR+1h_ABSOL.txt"
            

    elif type == 'temp' | type == 0:   # raw data reletive to confocal temperature experiments
        if percentage == 5:
            dye_after = 
            
        else percentage == 95:   # raw data reletive to confocal calcein experiments
            dye_after = 
            
    else type == 'none' | type == 3:
        if percentage == 5:
            dye_after = 
            
        else percentage == 95: 
            dye_after =

    if percentage == 5:
            dye_before = r"C:\Users\drb18182\Desktop\Docs\Data\confocal\MGG-165 [GPSomes, 5% % 95%, Gentle Hydation_v2, Lacc Nanoreactors\[IntProf] txt data\[IntProf] [AR ONLY] MGG165c_ 5 _AR+1h_ ABSOL.txt"
            
    elif percentage == 95:
            dye_before = r"C:\Users\drb18182\Desktop\Docs\Data\confocal\MGG-165 [GPSomes, 5% % 95%, Gentle Hydation_v2, Lacc Nanoreactors\[IntProf] txt data\[IntProf] [AR ONLY] MGG165c_ 95 _AR+1h_vesicles _ABSOL.txt"       
    
    return [dye_before, dye_after]
#############################

def main():
    #print('please select files...')
    #file_path_before = easygui.fileopenbox(msg="Choose a BEFORE file ", filetypes= "*.txt", multiple=True)
    #file_path_after = easygui.fileopenbox(msg="Choose an AFTER file", filetypes= "*.txt", multiple=True)

    files = [file_path_before,file_path_after]
    distance_before  = []
    intensity_before = []
    distance_after   = []
    intensity_after  = []



    for i in range(len(files)):
        
        raw_data = pd.read_csv(files[i][0], header=None, sep='\t', skiprows=3, na_values='-')
        raw_data = raw_data.apply(pd.to_numeric, errors='coerce')
        raw_data = raw_data.dropna(axis=1,how='all')    

        odd = list(range(1,raw_data.shape[1],2))
        even = list(range(0,raw_data.shape[1],2))

        x = raw_data.drop(columns = odd) 
        y = raw_data.drop(columns = even)
        
        if (i == 0):
            for i in x:
                a = recentre((x[i]*10**6).values.tolist()) # in µm
                distance_before.append(a) 

            for i in y:
                intensity_before.append(y[i].values.tolist())
        
        else:
            for i in x:
                b = recentre((x[i]*10**6).values.tolist()) # in µm
                distance_after.append(b) 

            for i in y:
                intensity_after.append(y[i].values.tolist())



    axis_font_size = 16
    label_font_size = 15
    c = ['tab:blue','tab:green','tab:red']


    rows = 1
    cols = 3
    fig, ax = plt.subplots(rows,cols, sharex=True, sharey=True, figsize=(10,3))
    titles = ['AT 5%','DT 5%','H 5%']

    for i in range(len(distance_before)):
        ax[i].plot(distance_before[i],intensity_before[i], linestyle='--', color = c[i], alpha = 0.5, label = '5%')
        ax[i].plot(distance_after[i],intensity_after[i],linestyle='-', color = c[i], alpha = 1, label = '95%')
        ax[i].set_title(titles[i], pad=30)
        ax[i].legend(loc='upper center', ncol = 2, bbox_to_anchor=(0, 0.97, 1, 0.2))#, mode = 'expand', ncol = 2)
        ax[i].xaxis.label.set_size(label_font_size)
        ax[i].yaxis.label.set_size(label_font_size)
        ax[i].xaxis.set_tick_params(labelsize=axis_font_size)
        ax[i].xaxis.set_tick_params(labelsize=axis_font_size)
        #ax[i].set_ylim(-0.01,1.3)
    ax[0].set_ylabel('Intensity (a.u.)')   
    ax[1].set_xlabel('Distance coordinates / µm')

    return