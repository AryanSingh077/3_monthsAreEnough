print("Day 1: Python for AI/ML");

# Arithmetic Operations (except complex where noted)

# + , - , * , / → normal arithmetic

# // → floor division (rounds down)

# % → remainder

# ** or pow() → power

# abs() → absolute value (magnitude for complex)

# divmod(x, y) → (x//y, x%y)

# Special points:

# // always rounds towards −∞

# int(float) truncates decimal part

# 0 ** 0 = 1 in Python

# int. float, str, bool, type() and type conversion

age = 19;
height = 5.9
name = "Aryan";
isStudent = True;

print(type(age));
print(type(height));
print(type(name));
print(type(isStudent));

input1 = int(input("Enter your age. : "))
input2 = float(input("Enter your height. : "))
input3 = str(input("Enter your name. : "))
input4 = bool(input("Enter your isStudent. : "))

print(f"My name is{name}, im {age} yrs old, my height is {height}, and im a {isStudent}");
print(type(input1));
print(type(input2));
print(type(input3));
print(type(input4));

