import fbchat
import time
import random
import string
import re

#uses the fbchat library found in the python package index to send messages via messenger
def spam(message):

	# fill in
	client = fbchat.Client("USERNAME", "PASSWORD")

	# looks for friends by name and takes the best one
	friends = client.getUsers("RECEIVER")
	friend = friends[0]

	#sending message
	sent = client.send(friend.uid, message)
	if(sent):
		print("Sent successfully")

	return

# reads the file and outputs the sentences
def readFile(txtFile):

	text = open(txtFile)
	raw = text.read()
	text = re.sub(r'(M|w{1,2})\.', r'\1', raw)
	sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
	return sentences

#not used. outputs a random word of variable length and variable characters
def randSpam():
	chars = random.randrange(0, 100)
	randString = ''.join(random.choice(string.lowercase + string.uppercase + string.digits) for _ in range(chars))
	return randString

def main():
	output = readFile("paradise.txt")
	for x in output:
		spam(x)
	return 

if __name__ == "__main__":
	main()
