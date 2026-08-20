# -*- coding: utf-8 -*-
import sys
import argparse
import cartopy
import pandas as pd
import xarray as xr
import datetime
import numpy as np
import os 
import geopandas as gpd
from shapely.geometry import Point
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.gridspec as gridspec
import dask.dataframe as dd
import pathlib
#from pylr2 import regress2

import sys
import argparse
import cartopy
import pandas as pd
import xarray as xr
import datetime
import numpy as np
import os 
import geopandas as gpd
import dask.dataframe as dd
import pathlib
from pathlib import Path

def main():
#    file_list=[\
#        'gud_cons_A.txt',\
#        'gud_cons_C.txt'\
#        'gud_cons_Fe.txt',\
#        'gud_cons_N.txt',\
#        'gud_cons_O.txt',\
#        'gud_cons_P.txt',\
#        'gud_cons_Si.txt'\
#        ]
    file_list=[\
        'darwin_cons_A.0000000000.txt',\
        'darwin_cons_C.0000000000.txt',\
        'darwin_cons_Fe.0000000000.txt',\
        'darwin_cons_N.0000000000.txt',\
        'darwin_cons_O.0000000000.txt',\
        'darwin_cons_P.0000000000.txt',\
        'darwin_cons_Si.0000000000.txt',\
        ]
    #dirpath=Path(str('/lustre/isaac24/scratch/ecarr/runs/V_08062025/run_25vDar_1D_UTK_tempfunV2_3882228/'))
    dirpath=pathlib.Path(args.rundir)
    print(dirpath, file = sys.stdout)
    rows=len(file_list)
    fig, axs = plt.subplots(nrows=rows,ncols=1, figsize=(10, 7.5))
    i=0
    for file in file_list:
        #file=file_list[1]
        con_file=pathlib.Path.joinpath(dirpath,file)
        #aa=Path(a).parts
        file_label=file.split('.')[0]
        print(con_file,i)
        
        f = open(con_file, 'r')
        line1 = f.readline()
        data_con = pd.read_csv(f, sep="\s+|\t+|\s+\t+|\t+\s+", names=line1.replace('#', '').split(), dtype=float)
        data_con['x']=data_con['iter']+0.1*data_con['stage']
        tot_mean=data_con['tot'].mean()
        #
        #data_con['nor_tot']=(data_con['tot']-data_con['tot'].mean())/data_con['tot'].std()
        #data_con['Mmean_tot']=(data_con['tot']-data_con['tot'].mean())
        #data_con['MM_tot']=(data_con['tot']-data_con['tot'].min())/(data_con['tot'].max()-data_con['tot'].min())
        #data_con['Mmedian_tot']=(data_con['tot']-data_con['tot'].median())
        data_con['PerFirst_tot']=((data_con['tot']-data_con['tot'][0])/data_con['tot'][0])*100
        axs[i].plot(data_con['x'],data_con['PerFirst_tot'])
        axs[i].set_ylim([-1, 1])
        axs[i].set_ylabel(str(file.split('.')[0].split('_')[2]))
        i=i+1
    filename=str('CONS_chk_percent')+str('.png')
    file_out=Path(filename)
    fig.savefig(file_out,dpi=300) 
    ####
    fig, axs = plt.subplots(nrows=rows,ncols=1, figsize=(10, 7.5))
    i=0
    for file in file_list:
        #file=file_list[1]
        con_file=pathlib.Path.joinpath(dirpath,file)
        file_label=file.split('.')[0]
        print(con_file,i)
        
        f = open(con_file, 'r')
        line1 = f.readline()
        data_con = pd.read_csv(f, sep="\s+|\t+|\s+\t+|\t+\s+", names=line1.replace('#', '').split(), dtype=float)
        data_con['x']=data_con['iter']+0.1*data_con['stage']
        tot_mean=data_con['tot'].mean()
        #
        data_con['nor_tot']=(data_con['tot']-data_con['tot'].mean())/data_con['tot'].std()
        #data_con['Mmean_tot']=(data_con['tot']-data_con['tot'].mean())
        #data_con['MM_tot']=(data_con['tot']-data_con['tot'].min())/(data_con['tot'].max()-data_con['tot'].min())
        #data_con['Mmedian_tot']=(data_con['tot']-data_con['tot'].median())
        #data_con['PerFirst_tot']=((data_con['tot']-data_con['tot'][0])/data_con['tot'][0])*100
        axs[i].plot(data_con['x'],data_con['tot'])
        axs[i].set_ylabel(str(file.split('.')[0].split('_')[2]))
        i=i+1
    filename=str('CONS_chk_tot')+str('.png')
    file_out=Path(filename)
    fig.savefig(file_out,dpi=300)  
        
    
########################
    print('EXIT  :: EXIT', flush=True, file = sys.stdout)
   
    
   
#
if __name__ == "__main__":
    #Initialize
    #Initialize
    parser=argparse.ArgumentParser(description="Run a check on Darwin model run")
     
    parser.add_argument('-dir',
                        '--rundir',
                        help="dir of model run",
                        required=True,
                        type=str)
    args = parser.parse_args()
    main()
