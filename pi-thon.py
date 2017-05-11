import os

f = open("pi-decimals.txt")
lines = f.readlines()
f.close()
pi = ""
for i in range(len(lines)):
	pi += lines[i].replace("\r", "").replace("\n", "")

answer = raw_input ("Enter pi from memory: ")
for i in range(len(answer)):
	if not answer[i] == pi[i]:
		break

print "Your score from memory:", i - 1
raw_input ("After pressing enter you will put in one more digit at a time")
os.system("clear")

while True:
	
	print pi[:i + 2]
	raw_input("press enter...")
	os.system("clear")
	answer = raw_input("")
	if answer == pi[:i+2]:
		os.system("clear")
		i += 1
	else:
		print "Wrong! correct answer:", pi[:i + 2]
		print "Your score is :", i
		input = raw_input("Continue? (Y/n) ")
		if input == "n":
			break
		else:
			i = 2
			os.system("clear")
