# students_count = 1000
# rating = 4.99
# is_published = True
# course_name = "Python programming"


# print(len(course))

# print(course[0], course[-1])
# print(course[9:])

# course = "python programmng"
# print(course.upper())
# # print(course)

# first_name = 'shiva'
# last_name = 'katti'
# # full_name = first_name + + last_name
# full_name = f"{first_name} {last_name}"
# print(full_name)
# print(full_name.upper())
# print(full_name.lower())
# print(full_name.title())
# print(full_name.strip())
# print(full_name.find("ti"))
# print(full_name.replace("ti", "TI"))
# print("shiv" in full_name)
# print("shiv" not in full_name)

# x = 1
# x = 1.1
# x = 1 + 2j

# print(round(2.9))

# print(round(2.6))

# x = input("x: ")
# y = int(x) + 1
# print(y)
# temperatue = 25
# if temperatue > 30:
#     print('very hot')
# elif temperatue > 20:
#     print('its nice')
# else:
#     print('normal day')

# age = 22
# # if age >= 18:
# #     print("Eligible")
# # else:
# #     print('not eligible')

# message = age

# and or not

# high_income = True
# good_credit = True

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("not eligible")

# for message in range(1, 10, 2):
#     print((message + 1) * ".")
# successful = False
# for message in range(3):
#     print("Attempt")
#     if successful:
#         print("successful")
#         break
# else:
#     print('Attempted 3 times and failed:(')

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# print(type(5))
# print(type(range(5))) # iterable,
# for x in "Siddarayajja":
#     print(x.upper())


# numner = 100
# while numner > 0:
#     print(numner)
#     numner //= 2

# command = ""
# while command.lower() != "quit":
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == 'quit':
#         break
# count = 0
# for x in range(1, 10):
#     if x % 2 == 0:
#         count += 1
#         print(x)
# print(f"we have {count} even numbers")


# writing own functions
# def greet():
#     print("learning py function")


# greet()

# arguments to functuons

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")


# greet("shiva", 'katti')

# def increment(number, by=1):
#     return number + by


# print(increment(2, by=2))

# result = (increment(2, 2))
# print(result)


# def multifly(*numbers):
#     total = 1
#     for number in numbers:
#         # print(number)
#         total = total * number
#     return total


# print(multifly(2, 3, 4, 5, 6))

# def save_user(**user):
#     print(user["name"])


# save_user(id=1, name="shiva", age=28)

# def greet():
#     message = "a"


# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FIZZBUZZ"
#     if input % 3 == 0:
#         return "FIZZ"
#     elif input % 5 == 0:
#         return "BUZZ"
#     return input


# print(fizz_buzz(1))


# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters[0:3])
# print(letters[::2])

# numbers = [1, 2, 3, 4, 5, 6, 7]
# first, second, *other = numbers
# print(first)
# print(other)
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# letters = ["a", "b", "c", "d"]
# for index, letter in enumerate(letters):
#     print(index, letter)

# letters.append("e")
# letters.insert(0, "aa")
# print(letters)

# print(letters.index("a"))

items = [
    ("product1", 10),
    ("product 2", 20),
    ("product 3", 9),
    ("product 4", 30),
]

prices = [item[1] for item in items]
print(prices)
x = list(filter(lambda item: item[1] >= 10, items))
print(x)
