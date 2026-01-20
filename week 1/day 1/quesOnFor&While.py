# Print numbers from 1 to 10.
for i in range(1,11):
    print(i)

# Print all even numbers between 1 and 50.

for i in range(1,51):
    if i%2==0:
        print(i)

# Find the sum of numbers from 1 to n (n from user).

n = int(input("Enter the no. : "))

sum = 0

for i in range(1,n+1):
    sum = sum +i
print(sum)

# Print the multiplication table of a number.

n = int(input("Enter the no. : "))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")

# Find the largest number in a list:

nums = [12, 45, 2, 89, 33]
grtNum = nums[0]

for i in nums:
    if i > grtNum:
        grtNum=i

print(f"greatest is {grtNum}")

# Print numbers from 1 to 5.
i =1
while i<=5:
    print(i)
    i += 1

# Reverse a number entered by the user.

n = int(input("Enter your no.: "))
rNum = 0

while n > 0:
    lDigit = n%10
    rNum = rNum*10 + lDigit
    n = n//10
print(rNum)

# Create a number guessing game (1–10).
code = 5

while True:
    n = int(input("Guess a no. btwn 1 to 10: "))
    if code == n:
        print("You guessed right")
        break
    else:
        print("You guessed wrong no.")

# q9:

while True:
    print(f'''Choose one:
1.Addition
2.Substraction
3.Multiplication
4.Division
5.Exit this loop.''')
    
    option = int(input("Enter the number: "))

    if option==5:
        print("Exiting the program.")
        break

    if option not in (1,2,3,4):
        print("Invalid input")
        continue

    num1 = int(input("Enter 1st no.:"))
    num2 = int(input("Enter 2nd no.:"))

    if option==1:
        print(f'''Addition: {num1 + num2}.''')
    elif option==2:
        print(f'''Substraction: {num1 - num2}.''')
    elif option==3:
        print(f'''Multiplication: {num1 * num2}.''')
    elif option==4:
        if num2==0:
            print("Not Defined")
        else:
            print(f'''Division: {num1 / num2}.''')
    else:
        print("Invalid input")
# q10:
i = 1
while i < 7:
    print(i)
    i += 1