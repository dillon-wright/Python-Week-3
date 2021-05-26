





pie_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
            "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]
y = ""
num = 1

for x in pie_list:

    y = y + "("+ str(num) +")" + " " + x + " "
    num = num + 1
print(y)