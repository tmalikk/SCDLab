# TASK 1

list_nos = []
print("Enter list of numbers")

for i in range(5):
    list_nos.append(int(input()))

print("Sum is:", sum(list_nos))


# TASK 2
for i in range(-4, 1):
    print(list_nos[-i])