category_list = []
n = int(input("How many categories would you like to track/budget: "))

for i in range(0, n):
    cat = input()
    category_list.append(cat)

print("Category list is: ", category_list)

dict = {}

for i in range(0, n):
    dict.update({category_list[i]: "0.0"})

for k, v in dict.items():
    dict[k] = float(v)

print("Dictionary: ", dict)
