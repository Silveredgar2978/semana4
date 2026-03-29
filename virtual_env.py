#virtual enviornments.

#they are to have a library version 1 in one and a library version 2 in the other
#if i install locally (globally) in my computer the same project will crash it would try to use both libraries.

#virtual env is an isolated bubble for each of the projects. inside those bubbles you install what you need. :)

#every professional python job uses one

##3 COMMANDS

#python3 -m venv .venv = creates a virtual enviornment inside a folder called .venv
#source .venv/bin/activate = activates it, now you are inside the bubble
#deactivate = exits the bubble

## when the enviornment is active the terminal will show (.venv) instead of >

#we don't want git to track the .venv folder because its huge, auto-generated, and different on every machine. everyone who clones my repo will create their own digital enviornment anyway

### total virtual env workflow

#enter a folder which already has your .venv folder, or create one
#activate by typing= source .venv/bin/activate you will know its activated when you see (.venv) in the terminal
#install your libraries, and work normally
#then when you're done just type= deactivate
