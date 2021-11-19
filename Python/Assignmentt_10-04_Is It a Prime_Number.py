num = int(input("Enter your number: "))

if num <= 1:
    print("Your number is lesser than 2, so it is not a prime number.")
else:
    for i in range(2,num):
        if num % i == 0: 
            print(num,"is not a prime number.")
            break
    else:
        print(num,"is a prime number.")i

