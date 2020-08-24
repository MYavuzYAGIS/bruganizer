
# MVP- minimum viable product
# CLI 1 input alacak
# bu inputun bir defaultu olacak
# 2 tane opsiyonu olacak
# birincisi c= copy ikincisi move=m

import os, shutil
import sys
import fnmatch
import click
from pyfiglet import Figlet, figlet_format
from termcolor import colored, cprint
import pathlib



@click.group(help='Select folder to be organized and give an argument copy or move')
@click.version_option(version='0.01' ,prog_name='Brute Organizer')
def main():
    color='cyan'
    banner='Brute Organizer'
    cprint(figlet_format(banner), color)
    #for styling and ASCII purposes.



@main.command()
@click.argument('folder')
@click.option('--extension' ,'-e', help='Specify the extension keyword to sort')
def copy(folder, extension):
    #copy takes 1 argument and 1 option.
    #/path/to/folder   and extension.
    for file in os.listdir(folder):
        name, ext = os.path.splitext(file)
        #separating the file and the extension and appointing the 2.item in the list to extension. 
        ext = ext[1:]
        # For each file we separately know the extension and the file name.
        if not fnmatch.fnmatch(file ,"*"+ext):
            click.echo("A file with a given extension does not found in the target folder")
            break
        #Checking whether there is a file with given extension
        elif fnmatch.fnmatch(file ,"*"+ext):
            click.secho(('Found File:{}'.format(file)+ext),fg='red' ,bold=True)
            #Flagging that file is found with the given extension
            if os.path.exists(os.path.join("sorted",ext,file)):
                    count =1
                    #/sorted/ext/file. 
                    for newlyAdded in os.listdir(os.path.join("sorted", ext, '')):
                        if name == "_".join(newlyAdded.split('.')[0].split('_')[:1]):
                        # generally downloaded files are stored as automatically numbered
                        # and separated by _. thus we splitted it    
                            count +=1
                            addedFile = name + '_' + str(count) + '.' + ext
                        else:
                            addedFile=file

            elif not os.path.exists(os.path.join("sorted",ext)):
                        os.makedirs(os.path.join("sorted",ext))
                        # If /sorted/ext is not existed, crate one.
                        click.secho(('Creating folder : Sorted') ,fg='red' ,bold=True)


                    
            else:
                    None
        print("Processing", file)
        shutil.copy(os.path.join(folder,file),
                    os.path.join("sorted",ext, file))
                    

        #file is being copied to the target destination
        #  Code gives error with the line below : TypeError: sequence item 2: expected str instance, tuple found
        # click.echo(click.style(('File:', os.path.join(file) + '>>>' + os.path.join("sorted", ext, file)),fg='red',bold= True))



# Copy and the Move options are basically function the same way, only shutil method is used differently. 
#Thus all the  commentaries are omitted below.



@main.command()
@click.argument('folder')
@click.option('--extension', '-e' ,help='Files in the pwd will be sorted')
def move(folder, extension):
    for file in os.listdir(folder):
        name, ext = os.path.splitext(file)
        ext = ext[1:]
        
        if not fnmatch.fnmatch(file ,"*"+ext):
            click.echo("A file with a given extension does not found in the target folder")
        
        elif fnmatch.fnmatch(file ,"*"+ext):
            click.secho(('Found File:{}'.format(file)),fg='red' ,bold=True)
            if os.path.exists(os.path.join("sorted",ext,file)):
                    count =1 
                    for newlyAdded in os.listdir(os.path.join("sorted", ext, '')):
                        if name == "_".join(newlyAdded.split('.')[0].split('_')[:1]):
                            count +=1
                            addedFile = name + '_' + str(count) + '.' + ext
                        else:
                            addedFile=file

            elif not os.path.exists(os.path.join("sorted",ext)):
                        os.makedirs(os.path.join("sorted",ext))
                        click.secho(('Creating folder : Sorted') ,fg='red' ,bold=True)
                    
            else:
                    None

        print("Processing", file)
        shutil.move(os.path.join(folder,file),
                    os.path.join("sorted",ext, file))
        
        #Code gives error with the line below  : TypeError: sequence item 2: expected str instance, tuple found
        #click.echo(click.style(('File:', os.path.join(file), '>>>', os.path.join("sorted", ext, file)),fg='red',bold= True))


if __name__ == '__main__':
    main()
