# README files

- when someone sees your repo in github the first thing they see is your README.md file. it's the front door of your project.

- its written in markdown, formatting language, you use symbols instead of buttons like in a docs

- markdown symbols i need to know= # = big heading, ## = subtitle, ### = smaller, **bold**, *italic*,`code` = code, - item for bullet point

example

# Auto FAQ Bot

A terminal-based AI tool that answers frequently asked questions
using the Anthropic API.

## What it does

- Takes a user question as input
- Sends it to Claude with a custom system prompt
- Returns a clear, focused answer
- Loops until the user types "quit"

## Requirements

- Python 3.10+
- An Anthropic API key

## How to run

1. Clone this repository
2. Install dependencies:
   pip install anthropic python-dotenv
3. Create a .env file with your API key:
   ANTHROPIC_API_KEY=your_key_here
4. Run the bot:
   python faq_bot.py

## Author

Silver — github.com/Silveredgar2978
