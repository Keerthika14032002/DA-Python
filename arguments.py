# numbs = [1,2,3,4,5]

# cal = list(map(lambda x:x*x, filter(lambda x: x%2 == 0, numbs)))

# print("cal", cal)


# users = [
#     {"name": "A", "marks": 80, "active": True},
#     {"name": "B", "marks":40, "active": False}
# ]

# res = list(filter(lambda u: u["active"] and u["marks"]> 79, users))

# print("res", res)


# products = [
#     {"name": "A", "price": 100},
#     {"name": "B", "price": 500},
#     {"name": "C", "price": 50}
# ]

# # Task:
# # 1. Filter price > 100
# # 2. Apply 10% discount
# # 3. Return final prices

# price = list(filter(lambda p: p["price"] > 100, products))
# dis = list(map(lambda d: d["price"]-(d["price"]*0.1), products))

# lambda expression: condition statements

# def num(x):
#     a = x**2
#     return a

# b = num(3)
# print("Square",b)

# square = lambda x,y: (x**2, y**3)
# a = square(3, 2)
# print("Square", a)





# def square(n):
#     return n*n



# square = lambda x: x*x


# print("square", square(5))



#March And June

# Dictionary

# {}

# contact_number = {
#     'Hari':1234567890,
#     'Joel': 8989898989,
#     'Kani': 7878787878
# }

# print("Search contact:", contact_number['Joel'])
# print("Search contact:", contact_number.get('Joel'))

# print("contact_number", contact_number)
# print("contact_number", contact_number.items())

# item = contact_number.items()

# keys = contact_number.keys()
# values = contact_number.values()

# print("Key", keys, "Value", values)
# print("Dict", contact_number)
# print("Item", item)
# for key, value in contact_number.items():
#     print("Key", key, "Value", value)

# contact_number['Hari'] = 9797979797
# print("c", contact_number)

# key = contact_number.keys()
# print("key", )
# l = list(key)[0] = 'Hari S'
# print("l", l)
# d = dict(l,)
# contact_number.update()


# contact_number["Hari S" ] = contact_number.pop("Hari")

# print("c", contact_number)


#Functions

# print("Hari pickup the coffee")
# print("Rooban pickup the coffee")
# print("Joel pickup the coffee")


# def functionname():

# def coffee(name):
#     print(name, "pickup the coffee")

# coffee('Hari')
# coffee('rooban')

# def welcome():
#     print("Welcome to DA Batch")


# welcome()
# welcome()



# def tour(name, place):
#     print(name, "-" ,place)

# tour("Rooban","Kerala")
# tour("Hari", "Kodaikanal")

# def kerala(name):
#     print(name, "Welcome to kerala")

# def kodaikanal(name):
#     print(name, "Welcome to Kodaikanal")

# def tour(name, place):
#     print(name, "Welcom to ",place)

# kerala("Hari")
# kodaikanal("Kani")
# tour("Hari", "Kerala")
# tour("Kani", "Kodaikanal")

# def price(costs):
#     gst = 0.18
#     total = costs+gst
#     return total

# print("Price", price(100))

# Types:

# without argument without return

# def welcom():
#     print("Wlcom to python class")

# welcom()

#with argument without return 

# def tour(place):
#     print("Welcome to", place)

# tour("Karnataka")

# without argument with return

# def cut_off():
#     marks = [89, 99, 98, 78, 99]
#     total = sum(marks)
#     percentage = (total/500)*100

#     return percentage

# print("cut off", cut_off())


# with argument with return
# def cut_off(marks1, marks2, marks3, marks4, marks5):
#     marks = [marks1, marks2, marks3, marks4, marks5]
#     total = sum(marks)
#     percentage = (total/500)*100

#     return percentage

# print("Percentage cut off", cut_off(97, 89, 98, 90, 80))


def sum(a,b):
    return a+b

print("Sum", sum(10, 5))