numbers=[]
for i in range(1,101):
    if i%15==0:
        numbers.append("FizzBuzz")
    elif i%3==0:
        numbers+=["Fizz"]
    elif i%5==0: 
        numbers+=["Buzz"]
    else:
        numbers+=[i]
print(numbers)
