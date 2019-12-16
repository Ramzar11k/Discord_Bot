from Riddle import HangMan
import random
import discord

TOKEN = <Token Here>

hangmanWords = ["immemorial", "reincarnation", "sandpaper", "incapacitated", "sleeve", "astrology", "triceratops", "smelt", "tempo", "pizza"]
client = discord.Client()
prefix = "-@-@-"
puzzle = None

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == prefix:
        msg = "Type -@-@-help for commands"
        await message.channel.send(msg)

    elif message.content.startswith(prefix):
        command = message.content[len(prefix):].split()
        command = [com.capitalize() for com in command]
        if command[0] == "Help":
            msg = "Add -@-@- before any command \n " \
                  "help - displays this, so, ironically, it doesn't really help that it's here \n " \
                  "hello - makes me say hello too, but don't expect me to start the conversation \n " \
                  "riddle - ??? \n" \
                  "hangman - ??? \n" \
                  "guess <letter> - try a letter for hangman"

        elif command[0] == "Hello":
            msg = 'Hello {0.author.mention}.'.format(message)

        elif command[0] == "Fuck_you":
            msg = "Fuck you too {0.author.mention}.".format(message)

        elif command[0] == "Riddle":
            msg = "What is like a square but round? \n" \
                  "To answer type '-@-@-answer ' followed by an answer \n" \
                  "Answer: One word"
        elif command[0] == "Answer":
            if command[1] == "Circle":
                msg = "Correct"
            else:
                msg = "Incorrect"

        elif command[0] == "Hangman":
            global puzzle
            puzzle = HangMan(hangmanWords[random.randint(0,len(hangmanWords)-1)])
            msg = " ".join(puzzle.puzzleWord)
        elif command[0] == "Guess":
            if puzzle is None:
                msg = "There is no active Hangman game \n" \
                      "To start one use -@-@-hangman"
            else:
                if len(command) != 2:
                    msg = "Guess must come in the form -@-@- <guess>"
                else:
                    msg = puzzle.guessLetter(command[1].lower())
            if puzzle is not None:
                if len(puzzle.letterToGuess) == 0:
                    msg = ("Congratz, the word was {}".format("".join(puzzle.fullWord)))
                    puzzle = None
                elif puzzle.lives == 0:
                    msg = ("You ran out of lives :(. The word was {}".format("".join(puzzle.fullWord)))
                    puzzle = None

        else:
            msg = "Unrecognized command, type -@-@-help for help."

        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(client.get_user(582373425809588245))



client.run(TOKEN)
