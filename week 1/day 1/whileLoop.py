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

i = 0
while i<=5:
    print(i)
    i += 1