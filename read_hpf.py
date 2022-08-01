import pandas
import glob
import subprocess

# MATLAB function
# function [ ] = plotdata( file )
# dos(['"C:\Program Files\Delsys, Inc\EMGworks 4.0 RC4\DelsysFileUtil.exe" -nogui -o CSV -i ' file]);
    
# data = csvread([file '.csv'], 1, 0);
# plot(data(:,1), data(:,2));
# end

DELSYS = r'C:\Program Files (x86)\Delsys, Inc\Delsys File Utility'
cmdline = 'DelsysFileUtil.exe'
args = ' -nogui -o CSV -i '

folder_Path  = r'C:\Users\Niamh Gill\OneDrive - English Institute of Sport\Data Folder\2022 07 27 - HS'
file_list = glob.glob(folder_Path + "/*.hpf")

n_count = len(file_list)
iCount = 1
for fileName in file_list:
    print("\nProcessing file: " + str(iCount) + '/' + str(n_count))
    inputStr = 'cmd /C ' + '"' + '"' + cmdline + '"' + args + '"' + fileName + '"' + '"'
    rc = subprocess.run(inputStr, cwd=DELSYS)
    iCount = iCount + 1
#     inputStr = 'cmd /C ' + '"' + '"' + DELSYS + cmdline + '"' + args + '"' + fileName + '"' + '"'
#     print("\nProcessing file: " + fileName)
#     rc = subprocess.run(inputStr, cwd=DELSYS) # run `cmdline` in `dir`