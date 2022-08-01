import glob
import subprocess

# Python version of the following MATLAB function 
# function [ ] = plotdata( file )
# dos(['"C:\Program Files\Delsys, Inc\EMGworks 4.0 RC4\DelsysFileUtil.exe" -nogui -o CSV -i ' file]);
    
# data = csvread([file '.csv'], 1, 0);
# plot(data(:,1), data(:,2));
# end

def hpf2csv(fileName):
    DELSYS = r'C:\Program Files (x86)\Delsys, Inc\Delsys File Utility'
    cmdline = 'DelsysFileUtil.exe'
    args = ' -nogui -o CSV -i '
    inputStr = 'cmd /C ' + '"' + '"' + cmdline + '"' + args + '"' + fileName + '"' + '"'
    rc = subprocess.run(inputStr, cwd=DELSYS)
