def seq(number: int, iterator: int):
    iterator -= 1
    if iterator != 0:
        number = number ** 2 - 1
        seq(number, iterator)
    else:
        print(number)
    return


while True:
    turn = int(input("მიმდევრობის მერამდენე წევრის ხილვა გსურთ : "))
    if turn >= 1:
        break
    else:
        print("გთხოვთ შემოიტანეთ ნატურალური რიცხვი")

seq(2, turn)
