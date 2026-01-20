# # Print numbers from 1 to 10.
# for i in range(1,11):
#     print(i)

# # Print all even numbers between 1 and 50.

# for i in range(1,51):
#     if i%2==0:
#         print(i)
#     else:
#         print()

# # Find the sum of numbers from 1 to n (n from user).

# n = int(input("Enter the no. : "))

# sum = 0

# for i in range(1,n):
#     sum = sum +i
#     print(sum)

# Print the multiplication table of a number.

# n = int(input("Enter the no. : "))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")

# Find the largest number in a list:

nums = [12, 45, 2, 89, 33]
grtNum = nums[0]

for i in nums:
    if i > grtNum:
        grtNum=i

print(f"greatest is {grtNum}")
