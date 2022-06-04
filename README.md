[![CodeFactor](https://www.codefactor.io/repository/github/myavuzyagis/bruganizer/badge)](https://www.codefactor.io/repository/github/myavuzyagis/bruganizer)


              ____             _          ___                        _
              | __ ) _ __ _   _| |_ ___   / _ \ _ __ __ _  __ _ _ __ (_)_______ _ __
              |  _ \| '__| | | | __/ _ \ | | | | '__/ _` |/ _` | '_ \| |_  / _ \ '__|
              | |_) | |  | |_| | ||  __/ | |_| | | | (_| | (_| | | | | |/ /  __/ |
              |____/|_|   \__,_|\__\___|  \___/|_|  \__, |\__,_|_| |_|_/___\___|_|
                                      |___/
        
**







**

            
                                                                        
 ![Image](https://github.com/Jubavicta/bruganizer/blob/master/savedpic.png)                                     

**
    
    
    
    
    
    
    
**


**What is Bruganizer?**

Bruganizer(Brute Organizer) is a tool written in python and is OS agnostic. It is powered with the click module for better integration with the terminal and offers better user experience. Moreover, it is not maintained in a form of script, but rather package so the user can call it regardless of their PWD.

**How to Install Bruganizer?**
**1- Installing Bruganizer**
You need `pipenv` and Python 3 in order to install and to use the  bruganizer.

If you're on MacOS, you can install Pipenv easily with Homebrew:
`$ brew install pipenv`

Or, if you're using Debian Buster+:
`$ sudo apt install pipenv`

Or, if you're using Fedora:
`$ sudo dnf install pipenv`

Or, if you're using FreeBSD:
`# pkg install py36-pipenv`

When none of the above is an option:
`$ pip install pipenv`

Check `https://docs.pipenv.org/` for more detailed information.

**2- Installing bruganizer**

Once pipenv is installed in the machine, install the `setuptools` with the command : `pipenv install setuptools`

then `cd` to the directory you want to store the script and run on the terminal :

`pipenv install git+https://github.com/Jubavicta/bruganizer.git`

if you do not install the `setuptools`, you need to give the flag `-e` to pipenv to read the requirements.


**make sure** that the user who runs the command and who installed the pipenv are the same!


**How to use bruganizer?**

Once its installed on the machine, now you can call the program just by typing `bruganizer`.

bruganizer requires 1 argument, which is the extension of the file you want to sort, if no extension is specified, the default option will sort all the files.

Also bruganizer can take either of 2 arguments, `copy` to copy the files or `move`to move them.

By default, it will sort the files within the CWD. However, a new path can also be given.


**Usage Example**

bruganier move /Users/user_home/Downloads -e pdf



**IMPORTANT NOTE: DIRECTORIES WHICH CONTAIN SUBDIRS RAISE ERRORS**











