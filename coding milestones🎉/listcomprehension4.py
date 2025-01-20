fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]#for each fruit, if it's no a banana just keep yhe fruit. But if it is a banana, change it to an orange.
print(newlist)