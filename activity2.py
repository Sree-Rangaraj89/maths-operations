number = int(input("Input your number:"))

def printfactors(number):
     print("The factors of given number is:")
     for i in range(1, number + 1):
        if number % i == 0:
            print(i)

printfactors(number)