## prob1:guessing game:

# code = 9

# while True:
#     guessedNo = int(input("Guess the number: "))
#     if guessedNo==code:
#         print("You guessed the right no.")
#         break
#     else:
#         print("Guessed no. is incorrect.")

# #prob2:meu driven program:

# while True:
#     print(f'''Choose one:
# 1.Addition
# 2.Substraction
# 3.Multiplication
# 4.Division
# 5.Exit this loop.''')
    
#     option = int(input("Enter the number: "))

#     if option==5:
#         print("Exiting the program.")
#         break

#     if option not in (1,2,3,4):
#         print("Invaliad input")
#         continue

#     num1 = int(input("Enter 1st no.:"))
#     num2 = int(input("Enter 2nd no.:"))

#     if option==1:
#         print(f'''Addition: {num1 + num2}.''')
#     elif option==2:
#         print(f'''Substraction: {num1 - num2}.''')
#     elif option==3:
#         print(f'''Multiplication: {num1 * num2}.''')
#     elif option==4:
#         if num2==0:
#             print("Not Defined")
#         else:
#             print(f'''Division: {num1 / num2}.''')
#     else:
#         print("Invalid input")
    
# prob3:infinte loop fixing:

# i = 0
# while i<=5:
#     print(i)
#     i += 1

# pelindrome no.

# n = int(input("Enter the no. : "))
# revN = 0

# while n > 0:
#     lDig = n%10 
#     revN = revN*10 + lDig
#     n = n//10
# print(revN)

#Buzz no: a no which ends with 7 or is divisible by 7:

# n = int(input("Enter your no. :"))

# if n % 10 == 7 or n % 7 == 0:
#     print("Entered no is Buzz no.")
# else:
#     print("Entered  no is not buzz no.")

##Armstrong no.: ex 153, a number that equals the sum of its own digits, each raised to the power of the total number of digits in the number

# n = int(input("Enter your no.: "))

# ldig = n%10

#Perfect no.: finds if a number is "perfect," meaning it equals the sum of its own proper divisors (factors excluding itself)

# pNo = int(input("Enter your no.: "))
# sum = 0
# for i in range(1, pNo+1):
#     if pNo % i == 0 and i<pNo:
#         num = i
#         sum = sum + i

# if sum == pNo:
#     print("No. is perfect no. ")
# else:
#     print("No. is not perfect")

#Neon no.: a number where the sum of the digits of its square equals the original number itself:

# num = int(input("Enter the no.: "))
# sq = num**2
# sum = 0
# anoSq = sq
# while anoSq>0:
#     dig = anoSq%10
#     sum = sum + dig
#     anoSq = anoSq //10

# if sum == num:
#     print(f"Entered no {num} is Neon no.")
# else:
#     print(f"Entred no {num} is not neon no.")


# #spy no: sum of digits equal to product of digit: ex 123:

# num = int(input("Enter your no.: "))
# dig = num
# sum = 0
# pro = 1
# while dig>0:
#     dig1 = dig%10
#     sum = sum + dig1
#     pro = pro*dig1
#     dig = dig//10

# if sum == pro:
#     print("Neon no.")
# else:
#     print("Not Neon no.")

# Automorphic no.: a number whose square ends with the original number itself

# num = int(input("Enter your no. : "))
# sq = num**2
# ldig = sq%10

# if ldig == num:
#     print("Automorphic no.")
# else:
#     print("NOT Automorphic")

#Harshad(niven) no. : no div by sum of its digits:

# num = int(input("Enter your no.: "))
# sum = 0
# dig = num

# while dig>0:
#     ldig = dig%10
#     sum = sum + ldig
#     dig = dig//10

# if num%sum==0:
#     print("Digit is Harshad no.")
# else:
#     print("Digit not Harshad no.")

#krishnamurthy no.: a number where the sum of the factorials of its digits is equal to the original number itself.

num = int(input("Enter your no."))

sum = 0
dig = num

while dig > 0:
    ldig = dig%10
    i = 1
    fact = 1
    while i<ldig+1:
        fact = fact*i
        i +=1
    sum = sum + fact
    dig = dig//10

if sum == num:
    print("Krishnamurthy no.")
else:
    print("Not Krishnamurthy no.")