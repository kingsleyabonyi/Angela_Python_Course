n = int(input("Check for this number: "))
def prime_checker(number):
    for i in range(2, number):

        if number % i == 0:
            print("is not a prime number")
        else:
            print("It is a prime number")

prime_checker(n)