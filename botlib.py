import random

# Admin name(s) for certain commands
# Usage:
#       if sender in ADMINS:
#           myfunc()
ADMINS = ("SlimTim10", "Z_Mass")

def parsemsg(privmsg):
# Split the received PRIVMSG message into two useful parts
# Example message:
#   :SlimTim10!~SlimTim10@127-0-0-1.network.com PRIVMSG #channel :Hello?
    parts = privmsg[1:].split(':', 1)
# The information part of the message (sender, "PRIVMSG", channel/nickname)
    info = parts[0].split(' ')
    msg = parts[1].rstrip()	# The message part (e.g., "Hello?")
# The sender of the message (e.g., "SlimTim10")
    sender = info[0].split('!')[0]
# The string to be returned
    ret = ''

# Treat messages starting with '!' as commands (e.g., "!say hi")
    if msg[0] == '!':
# Split command message into two parts: bot command and following text
        cmd = msg.split(' ', 1)

# The '!say' command makes the bot say something
# To-do: make this command work for private messages sent directly to the bot
        if cmd[0] == '!say':
# Send the message to where the '!say' command was sent
            ret = 'PRIVMSG ' + info[2] + ' :' + cmd[1] + '\n'

# The '!die' command makes the bot quit (admin command)
        if cmd[0] == '!die' and sender in ADMINS:
            ret = 'QUIT\n'

# To-do: add a '!calc' command that evaluates basic mathematical expressions
# Difficulty: easy

# To-do: add a '!insult' command that makes the bot say a randomly selected
# 	insult to the command sender
# Difficulty: easy

# To-do: find and fix the bug
# To-do: add helpful comments to this command's code
        if cmd[0] == '!rps':
            try:
                user_rps = int(cmd[1])
                if user_rps < 0 or user_rps > 3:
                    raise Exception("Invalid")
                else:
                    rps_names = ['rock', 'paper', 'scissors']
                    bot_rps = random.randint(0, 3)
                    ret = 'PRIVMSG ' + info[2] + ' :Player chose ' + \
                    rps_names[user_rps] + '. LPMCBot chose ' + \
                    rps_names[bot_rps] + '. '
                    if user_rps == bot_rps:
                        ret += 'Tie game.\n'
                    else:
                        if user_rps == (bot_rps + 1) % 3:
                            ret += 'Player wins!\n'
                        else:
                            ret += 'Player loses.\n'
            except:
                ret = 'PRIVMSG ' + info[2] + \
                ' :Command help: 0 = Rock, 1 = Paper, 3 = Scissors. ' + \
                'Example: !rps 1\n'


# To-do: add a '!ttt' command that starts a game of Tic Tac Toe to be played
# 	against the bot
# Difficulty: hard

    return ret			# Return the appropriate string
