import os
import shutil
import numpy as np

#change working directory to replays folder
replays_directory = '/Users/spnck/downloads/replays/'
replays_directory_new = '/Users/spnck/downloads/replays_new/'
os.chdir(replays_directory)

#create a folder function
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

#STEP1: create folders with names numbered 1-84
replay_count = (len(os.listdir()) / 2) + 1
os.chdir(replays_directory_new)
folder_amount = np.arange(1, replay_count)
folder_names = list(map(str, folder_amount)) 

for name in folder_names:
    createFolder(name)

print('Folders Generated')
    
#STEP2: move files into respective folders
os.chdir(replays_directory)
demos = os.listdir(replays_directory)
folder_names_double = np.repeat(folder_names, 2)

for match, name in zip(demos, folder_names_double):
    old_directory = replays_directory + match
    new_directory = replays_directory_new + name
    shutil.move(old_directory, new_directory + '/' + match)
    
print('Demos Moved')
