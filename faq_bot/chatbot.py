# AUTO FAQ BOT
# ------------
# Build a terminal chatbot that does all of this:
#
# 1. Has a SYSTEM PROMPT that defines the bot's personality and topic.
#    Example: "You are a helpful assistant that only answers questions about Python programming."
#    You choose the topic — make it something you find interesting.
#
# 2. Asks the user to type a question
#
# 3. Sends the question to the Gemini API (use your working code from 4_exercise.py as reference)
#
# 4. Prints the response
#
# 5. Keeps looping until the user types "quit"
#
# 6. When the user types "quit", print "Goodbye!" and exit cleanly
#
# 7. Handles errors properly — at minimum: API errors and empty input
#
# 8. Loads the API key from a .env file — never hardcode it
#
# REQUIREMENTS:
# - Use a system prompt that gives the bot a clear personality and topic
# - Use functions — do not write everything in one block
# - The code must be clean and commented
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

#to load the API key inside the .env file, you can see example in .env.example
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")   #saves api key
client = genai.Client(api_key=API_KEY)  #states google ai client


def main():
    print("Welcome to the numbers chatbot")
    while True:     #starts infinite loop

        user_question = input("Type a question or type \"quit\" if you are done- ")

        if user_question.strip() == "":     #to handle empty questions
            print("type something brother")
            continue        #skips the loop and goes back to the top to start again
        elif user_question == "quit":   #handles exiting of the loop
            print("good day brother")
            break           
        else:                                   #system prompt
            print(system_prompt(user_question, "you are an assistant that only talks with numbers"))    #calls system_prompt function below

            
#fuction to give gemini previous SYSTEM PROMPT that defines what it does. and gets a question to answer too.
def system_prompt(user_question, prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=prompt),
            contents=user_question
        )
        return response.text      #returns the response in text to print
    except Exception as e:  #e is error message
        print(f"there was an error brudda {e}") # {e} shows the error
        return  #returns nothing to go back to the main loop



main()