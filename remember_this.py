remember_list = []

print("What do you need to remember?")
print('''Put your input in "quotation marks"''')
print("""Type "DONE" when you're done.""")

while True:
	remember = input("~~ ")
	if remember == "DONE":
		break
	remember_list.append(remember)

print("Remember to: ")
for item in remember_list:
	print(item)