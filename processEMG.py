import pandas
import glob
import subprocess
from read_hpf import hpf2csv

folder_Path  = r'C:\Users\Niamh Gill\OneDrive - English Institute of Sport\Data Folder\2022 07 27 - HS'

file_list = glob.glob(folder_Path + "/*.hpf")

n_count = len(file_list)
iCount = 1
for fileName in file_list:
    print("\nProcessing file: " + str(iCount) + '/' + str(n_count))
    hpf2csv(fileName)
    iCount = iCount + 1
