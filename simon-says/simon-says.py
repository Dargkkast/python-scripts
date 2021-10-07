import random
list = ["red","blue","yellow","green","black","white","pink","brown"]


while True:
	simon = random.choice(list)
	print("Simon says... " + simon + "(Exit to leave)")

	str = input()

	if str.casefold() == "exit":
		print("Bye then.")
		break

	if str.casefold() == simon.casefold():
		print("Not bad, how about this...")
	else :
		print("DOOOOOOM!")
