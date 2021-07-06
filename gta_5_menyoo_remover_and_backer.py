import os 
import shutil
import copy
from distutils.dir_util import copy_tree
import glob
import string

list_of_files =[]

#this function will collect 
#the list of filename and add each file to list_of_files (global variable)
def get_file_list():
    files = os.listdir(os.curdir)
    for f in files:
        list_of_files.append(f)

#Basically this will copy all the contents in Mod Folder
def copy_file():
    #Current Mod folder
    current_directory =os.getcwd()
    #gta 5 folder
    parent_directory=os.path.dirname(current_directory)
 

    os.chdir(os.path.dirname(__file__))
    print("Copying Mod Files in Gta 5 Directory")
    copy_tree(current_directory,  parent_directory) 
    if copy_tree(current_directory,  parent_directory):
        print("Done! Copying Files.")
    else:
        print("Error Copying")

# this function 
# scan if file exist in list_of_files(global list) then delete it
def remove_mod():
    #gta 5 folder
    current_directory =os.getcwd()
    dir ="D:\\Users\\Rj\\Documents\\Pythoners\\1Copyhere\\" 
   
    parent_directory=os.path.dirname(current_directory)
    scan_folder =os.listdir(parent_directory)
    list_of_deletion=[]   
    for f in list_of_files:
        if f in scan_folder:
            list_of_deletion.append(parent_directory+"\\"+f)
    for l in list_of_deletion:
         try:
             shutil.rmtree(l)
         except:
             os.remove(l)
    print ("Done Removing")


        
answ =input("Enter Y to delete the meenyo MOD or Enter M to activate menyoo MOD\n")
if answ == 'Y' or answ == 'y':
    get_file_list()
    remove_mod()
elif answ == 'M' or answ == 'm':
    copy_file()








