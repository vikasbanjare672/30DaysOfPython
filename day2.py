''' Exercises: Level 1
1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line '''


print("Day 2: 30 Days of python programming")
first_name = "Vikas"
last_name = "ss"
full_name = first_name + " " + last_name
country = "India"
city = "New Delhi maybe"
age = "MEMEOW!!"
year = 2023
is_married = False
is_true = True
is_light_on = True
cat , dog , mouse = "cat" , "dog" , "mouse"






'''Exercises: Level 2
1. Check the data type of all your variables using type() built-in function
2. Using the len) built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
5. Add num_one and num_two and assign the value to a variable total
6. Subtract num_two from num_one and assign the value to a variable diff
7. Multiply num_two and num_one and assign the value to a variable product
8. Divide num_one by num_two and assign the value to a variable division
9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10. Calculate num_one to the power of num_two and assign the value to a variable exp
11. Find floor division of num_one by num_two and assign the value to a variable floor_division
12. The radius of a circle is 30 meters:
        i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
        ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        iii. Take radius as user input and calculate the area.
13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords '''



print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(cat))
print(type(dog))
print(type(mouse))

f_name_length = len(first_name)
l_name_length = len(last_name)
diff_length = f_name_length - l_name_length
print("Length of first name:", f_name_length)
print("Length of last name:", l_name_length)
print("Difference in length:", diff_length)
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = int(input("Enter the radius of the circle: "))
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print("Area of the circle:", area_of_circle)
print("Circumference of the circle:", circum_of_circle)

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
country_input = input("Enter your country: ")
age_input = input("Enter your age: ")

print("new first name:", fname)
print("new last name:", lname)
print("new country:", country_input)
print("new age:", age_input)