
# Arithmetic operators, Comparison operators,Logical operators 
#1. Arithmetic ope: +,-,*,**,%(returns remainder), //(returns integer value, ignores decimals), /
#2. Comparison ope: == equal to,not eq to !=,less than and eq to <=,greater than and eq to >=,less than <,greater than >.
#3. Logical ope: or(checks 2nd value if first is false), and(checks 2nd value if 1st is true), not(reverse).
# "="is used as assingment ope and "==" is equal to ope.

# prob 1: Even/ Odd checker:
#for even 
# n = int(input("Enter your no. :"))
# even = n%2 == 0
# odd  = n%2 != 0
# print(f"no. is even: {even}, its odd: {odd}");

# # this is not a good way of coding:

# if(n%2==0):
#     print("No. is even")
# else:
#     print("No. is odd.")

#prob 2: Greater than three numbers:

a = int(input("Enter your no. : "));
b = int(input("Enter your no. : "));
c = int(input("Enter your no. : "));

if a>=b and a>=c:
    print("a is greatest")
elif b>=a and b>=c:
    print("b is greatest")
else:
    print("c is greatest");

