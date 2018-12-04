# ARPNLP


##Installation

To be able to run this project, you need to have a number of things installed (at least verified with):
 - Python 3.7
 - Pipenv, which is used for virtual envs and package management
 - A C compiler, Google is your friend, should work with Visual Studio C compiler
 - An API key from newsapi.org, as a developer you can get one for free (limit to 1000 requests/day)
 
After you have installed all of the above, do the following:

 - `pipenv --python3.7` which creates a virtual enviroment
 - `pipenv install` which installs the packages as defined by the devlopers in the Pipfile
 - `pipenv run python -m spacy download en` which downloads the english pre-trained models of spacy
 
If one decides to use a normal Virtual Env with pip, or installs system wide, you can also do this using the requirements.txt file. You will still need a C compiler, and run the last command (without the pipenv run)

You also need to create a file API.py, which is only used to define the variable API_KEY (we don't commit that file, it is linked ot you as a person!)
 
