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

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def main():
