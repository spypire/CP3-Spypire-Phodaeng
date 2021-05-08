Apple = 10
Banana = 20
carrot = 30
username = input("username :")
password = input("password :")
if username == "spypire" and password == "1234":
    print("----ishop----")
    print("----menu----")
    print("1.  Banana   :  20 THB")
    print("2.  Apple    :  10 THB")
    print("3.  carrot   :  30 THB")
    select_product = int(input("อยากหม่ำอะไรดีครับ >>"))
    if select_product == 1:
        fruit = "apple"
        number = int(input("จำนวน :"))
        price = Apple*number
    elif select_product == 2:
        fruit = "Banana"
        number = int(input("จำนวน :"))
        price = Banana * number
    elif select_product == 3:
        fruit = "carrot"
        number = int(input("จำนวน :"))
        price = carrot * number
    print(fruit, "จำนวน", number,"ราคา",price,"THB")
    print("ขอบคุณที่ใช้บริการ")
else:
    print("Error")