#
# to add tave I had to assign the 360 day cal to the NC, i also inc it version for compression   
# nccopy -k netCDF-4 -d 2 -s tave.0000000000.t001.nc tave.nc
# ncatted -a calendar,T,c,c,'360_day' tave.nc 
 


