# -*- coding: utf-8 -*-
import sys
import argparse
import pathlib
import csv

def get_value_darwintxt(file,var_string):
    chk_next=False
    save_l_no=-9999
    save_line=str('-9999')
    with open(file, 'r') as fp:
        for l_no, line in enumerate(fp):
            # search string
            if chk_next:
                #print(line)
                if line[1].isspace():
                    #print('indent found')
                    save_line=str(save_line)+str(line.rstrip())
                    chk_next=True
                else:
                    #print('string found in a file')
                    #print('Line Number:', save_l_no)
                    #print('Line:', save_line)
                    # don't look for next lines
                    break
            elif var_string in line:
                #print(line)
                save_l_no=l_no
                save_line=line.rstrip()
                chk_next=True
    
    csv_line= save_line.replace('=',',').rstrip()
    csv_line= csv_line.replace(' ','')
    return(csv_line)


#from figcom import get_value_darwintxt
def main():
    #
   
    PD_base=pathlib.Path(str(args.basedir))
    #
    filename_traits=str('darwin_traits.txt')
    file_traits=PD_base.joinpath(filename_traits)
    #
    virus_file=PD_base.joinpath('virus_data.csv')
    with open(virus_file, 'a', newline='') as csvfile:
        var_string=str('V_ABSORP')
        ret_line=get_value_darwintxt(file_traits,var_string)
        #print(ret_line)
        csvfile.write(ret_line)
        csvfile.write("\n")
        var_string=str('V_ABEFF')
        ret_line=get_value_darwintxt(file_traits,var_string)
        #print(ret_line)
        csvfile.write(ret_line)
        csvfile.write("\n")
        var_string=str('V_LATENT')
        ret_line=get_value_darwintxt(file_traits,var_string)
        #print(ret_line)
        csvfile.write(ret_line)
        csvfile.write("\n")
        var_string=str('V_BURST')
        ret_line=get_value_darwintxt(file_traits,var_string)
        #print(ret_line)
        csvfile.write(ret_line)
        csvfile.write("\n")
        var_string=str('V_DOMPOMFRAC')
        ret_line=get_value_darwintxt(file_traits,var_string)
        #print(ret_line)
        csvfile.write(ret_line)
        csvfile.write("\n")
        
    ########################
    print('EXIT  :: EXIT', flush=True, file = sys.stdout)
   
    
   
#
if __name__ == "__main__":
    #Initialize
    parser=argparse.ArgumentParser(description="Extract virus data to csv file")
 
    #Adding optional parameters
    parser.add_argument('-base',
                        '--basedir',
                        help="base dir of model run",
                        required=True,
                        type=str)
    
    args = parser.parse_args()
    
    main()
