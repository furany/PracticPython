spam =[]
while True:
    print("Namen deiner Katze nummer: " +str(len(spam)+1)+ " oder LEER wenn fertig")
    name = input()
    if name == "":
        break
    spam = spam + [name]

print("Die Namen deiner Katzen sind: ")
for name in spam:
    print(" "+name)
