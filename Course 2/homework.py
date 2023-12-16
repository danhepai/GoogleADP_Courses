num_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

print("Sorted list ascending:", sorted(num_list))  # ascending order
print("Sorted list descending:", sorted(num_list, reverse=True))  # descending order

print("Printing the els with even indexes:", num_list[::2])  # printing the els with even indexes
print("Printing the els with odd indexes:", num_list[1::2])  # printing the els with odd indexes

print("Multiple of 3 from list: ", end="")
for element in num_list:
    if element % 3 == 0:
        print(element, end=", ")
