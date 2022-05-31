n = int(input("Enter a number: "))

if n > 1:
    for j in range(2, n):
        if (n % j) == 0:
            print("The number is NOT a prime number")

            break
    else:
        print("The number is a prime number")

else:
    print("The number is NOT a prime number")