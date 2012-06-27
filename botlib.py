# To-do: allow for multiple admins (make all the appropriate changes in code)
ADMIN = "SlimTim10"			# Admin name(s) for certain commands

def parsemsg(privmsg):
# Split the received PRIVMSG message into two useful parts
# Example message:
# 	:SlimTim10!~SlimTim10@127-0-0-1.network.com PRIVMSG #channel :Hello?
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
		if cmd[0] == '!die' and sender == ADMIN:
			ret = 'QUIT\n'

	return ret