# .env files

#i used in semana 3, they are used to store api keys and important stuff you don't want people to see in your repo.

#you add .env to the .gitignore file for that

##and TO USE we used:

# from dotenv import load_dotenv
# import os

# load_dotenv()
# API_KEY = os.getenv("ANTHROPIC_API_KEY")

##now we can use the API_KEY variable where our key goes in the project

### now the thing we haven't yet seen is requirements.txt they are to tell people all the libraries they need to install for your project
#with requirements.txt they can just install all of the required libraries in one go and here is how.

#first you type=       pip freeze > requirements.txt     in the terminal
#we type all of this because it will automatically add all of your downloaded libraries there.
# pip freeze (lists all the downloaded pips), > (moves to the right), requirements.txt(is the file where every pip install is going to go)
#for everyone that clones your repo they run= pip install -r requirements.txt   and they get everything they need.

### another thing they havent seen is the .env.example, its just a file in your repo that represents how your real env is placed. so that they can fill out the missing info and make it their .env file. this is because you can't share your real .env file.

#ex(inside the .env.example file). ANTHROPIC_API_KEY=your_key_here
