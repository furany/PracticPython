print("n(n+1)/2) Enter n:")
try:
    num = int(input())+1
    total= 0
    for i in range (num):
        total = total + i
    print(total)
except ValueError:
    print("You did not enter a number")
input("Press enter to exit ;)") #
