# Store marks in list
# Calculate average
# Find max/min manually

marks = []
for i in range(6):
    inMarks = int(input("Enter your marks: "))
    marks.append(inMarks)
print(marks)

total = 0
for m in marks:
    total = total + m

ave = total/len(marks)
print("Average marks:", ave)

maxMa = marks[0]
for m in marks:
    if m > maxMa:
        maxMa = m
# maxMarks = max(marks)
print("Max marks are: ",maxMa)