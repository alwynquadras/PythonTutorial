print("Program for sorting the marks of given student")
list = []
i = 0
n = int(input("Enter the number of students:"))
while i < n:
    a = input(f"enter the marks of student{i+1}: ")
    list.append(a)
    i += 1
print("The give list of marks are: ",list)
list.sort()
print("sorting the list...........................")
print("here is your list",list)


