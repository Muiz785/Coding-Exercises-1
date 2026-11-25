

#Exercise 1:City list
# cities = ["Lahore" , "Karachi" , "Multan" , "Quetta" , "Peshawar"]
# print(cities[0])
# print(cities[-1])
# print(cities[1:4])
# print(cities[::-1])



#Exercise 3:Shopping list
# shopping_list = ["milk", "bread", "eggs"]
# print(shopping_list)
# shopping_list.append("rice")
# print(shopping_list)
# shopping_list.insert(1, "sugar")
# print(shopping_list)
# shopping_list.remove("milk")
# print(shopping_list)
# popped_item = shopping_list.pop()
# print("Popped item:", popped_item)
# print("Final list:", shopping_list)



#Exercise 5:Even and odds
# numbers =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# even_numbers =[2,4,6,8,10,12,14]
# print(even_numbers)
# odd_numbers =[1,3,5,7,9,11,13,15]
# print(odd_numbers)


#Exercise 6:Rotate a list
# r=[1,2,3,4,5]
# print(r)
# r=r[-1:]+r[:-1]
# print(r)



#Exercise 2:Marks Report
# marks =[78,92,65,88,54]
# total_marks = sum(marks)
# average_marks = total_marks/len(marks)
# highest_marks = max(marks)
# lowest_marks = min(marks)

# count = 0
# for mark in marks:
#     if mark >= 70:
#         count += 1

# print("Total_marks:" , total_marks)   
# print("Average_marks:", average_marks)
# print("Highest_marks:", highest_marks)
# print("Lowest_marks:", lowest_marks)
# print("Marks above 70:",count)



#Exercise 4:Remove duplicates
# nums=[3,1,3,2,1,5]
# unique_nums = []
# for num in nums:
#     if num not in unique_nums:
#         unique_nums.append(num)
# print(unique_nums)



#Exercise 7: Copy or not?
# a= [1,2,3]

# b= a
# c= a.copy()

# a.append(4)
# print("a:", a)
# print("b:", b)
# print("c:", c)

# b changed because b and a refer to same list.
# c did not change because a.copy() created a seperate list.



#Exercise 11:Second highest
# scores = [45,82,67,91,73]
# highest= 0
# second_highest=0

# for score in scores:
#     if score > highest:
#         second_highest =highest
#         highest = score 

#     elif score > second_highest:
#         second_highest = score
# print("Second Highest:" , second_highest)



#Exercise 10:List  of tuples
# students = [("Ali",85),("Sara",92),("Ahmed",76),("Hina",64)]
# for name,marks in students:
#     print(name,"scored",marks) 
# def get_marks(s):
#     return s[1]
# topper=max(students,key=get_marks)
# print("topper",topper[0],topper[1])
# passed =[name for name,marks in students if marks >= 70]
# print("passed",passed)



# Exercise 9:Vote counter
# votes = ("A","B","A","C","A","B")
# a = votes.count("A")
# b = votes.count("B")
# c = votes.count("C")

# print("A =", a)
# print("B =", b)
# print("C =", c)

# pos = votes.index("C")
# print("first C at index", pos)



# Exercise  8:Student Record
# student = ("BSIT-12", "Sara",88)
# roll_no, name, marks =student
# print(f"Roll no: {roll_no}")
# print(f"Name: {name}")
# print(f"Marks: {marks}")

# try:
#     student[2] = 95
# except TypeError as e:
#     print("Error:", e)
# # Error: TypeError: 'tuple' object does not support item assignment

# temp = list(student)
# temp[2] = 95
# student = tuple(temp)
# print(student)


      






