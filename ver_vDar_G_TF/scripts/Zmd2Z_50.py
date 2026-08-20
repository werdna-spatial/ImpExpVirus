# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:32:21 2022

@author: eric
"""

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

def main():
    
    gridfile=args.gridfilename
    print(gridfile, file = sys.stdout)
    inputfile=args.inputfilename
    print(inputfile, file = sys.stdout)
    outputfile=args.outputfilename
    print(outputfile, file = sys.stdout)
    
    #PD_NC=pathlib.Path('./')
    #os.chdir(PD_NC)
    #
    ds_grid=xr.open_mfdataset(gridfile,  combine='by_coords', parallel=False,chunks={'T':1,'Z':1})
    depth_values=np.array(ds_grid.Z.values)
    #pre='3d'
    #post='Z3d'
    I_name=inputfile
    O_name=outputfile
    ds_tracers=xr.open_mfdataset(I_name,  combine='by_coords', parallel=False,chunks={'T':1,'Z':1})
    print(list(ds_tracers), file = sys.stdout)
    ds_tracersZ=ds_tracers.rename({str('Zmd000050'):str('Z')})
    ds_tracersZ=ds_tracersZ.assign_coords(Z=depth_values)
    ds_tracersZ.to_netcdf(path=O_name)
    ds_tracers.close()
    ds_tracersZ.close()
    ########################
    #
    print('EXIT  :: EXIT', flush=True, file = sys.stdout)
   
    
   
#
if __name__ == "__main__":
    #Initialize
    #Initialize
    parser=argparse.ArgumentParser(description="Rename Depth attribute in NC file from Zmd to Z.  Need for comforty between tracers and diagnostics")
     
    #Adding optional parameters
    parser.add_argument('-grid',
                        '--gridfilename',
                        help="grid nc file",
                        required=True,
                        type=str)
    parser.add_argument('-fin',
                        '--inputfilename',
                        help="in name of nc file",
                        required=True,
                        type=str)
    parser.add_argument('-fout',
                     '--outputfilename',
                     help="out name of nc file",
                     required=True,
                     type=str)
 
    args = parser.parse_args()
    
    main()
