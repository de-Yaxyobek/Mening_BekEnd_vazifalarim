# # append bilan ishlash
# # 1-misol
# mevalar = []
# mevalar.append("olma")  
# mevalar.append("anor")
# mevalar.append("shaftoli")
# mevalar.append("o'rik")
# mevalar.append("banan")
# print(mevalar)
# # 2-misol
# mevalar.append("yo'lbars")
# mevalar.append("sher")
# mevalar.append("qoplon")
# print(mevalar)
# # 3-misol
# mevalar.append("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
# print(mevalar)
# # 4-misol
# mevalar = ["olma", "anor", "shaftoli", "o'rik", "banan"]
# mevalar.append("anjir")
# print(mevalar)
# # 5-misol
# name1 = input("1-Ismingiz nima? ")
# name2 = input("2-Ismingiz nima? ")
# name3 = input("3-Ismingiz nima? ")
# mevalar.append(name1,name2,name3)
# print(mevalar)

# # inset blan ishlash
# # 6-misol
# numbers = ['1', '2', '3', '4', '5']
# numbers.insert(0, '0')
# print(numbers)
# # 7-misol
# mevalar = ["olma", "anor", "shaftoli", "o'rik", "banan"]
# mevalar.insert(1, "tarvuz")
# print(mevalar)
# # 8-misol
# numbers.insert(-3, '2.5')
# print(numbers)
# # 9-misol
# numbers.insert(-1, 'Yahyobek')
# numbers.insert(-1, 'Laziz')
# numbers.insert(-1, 'Azizbek')
# print(numbers)
# # 10-misol
# name = input("Ismingiz kiriting: ")
# names = ['Laziz', 'Mahmudjon', 'Husan', 'Yahyobek']
# names.insert(0, name)
# print(names)

# # del bilan ishlash
# # 11-misol
# numbers = ['1', '2', '3', '4', '5']
# del numbers[2]
# print(numbers)
# # 12-misol
# mevalar = ["olma", "anor", "shaftoli", "o'rik", "banan"]
# del mevalar[0]
# print(mevalar)
# # 13-misol
# sonlar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# del sonlar[-1]
# print(sonlar)
# # 14-misol
# sonlar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# del sonlar[1:3]
# print(sonlar)
# # 15-misol
# mevalar = ["olma", "anor", "shaftoli", "o'rik", "banan"]
# del mevalar[0:5]
# print(mevalar)

# # remove bilan ishlash
# # 16-misol
# fruits = ["olma", "anor", "shaftoli", "o'rik", "banan"]
# fruits.remove("anor")
# print(fruits)
# # 17-misol
# colors = ["qizil", "qizil", "qizil"]
# colors.remove("qizil")
# print(colors)
# # 18-misol
# sonlar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# son = input("Raqam kiriting: ")
# sonlar.remove(son)
# print(sonlar)
# # 19-misol
# animals = ["it", "mushuk", "quyon", "to'ng'iz", "sigir"]
# animals.remove("quyon")
# print(animals)
# # 20-misol
# mevalar = ["olma", "anor", "shaftoli", "o'rik", "banan"]
# mevalar.remove("anjir")
# print(mevalar)
# # bunaqada xato beradi yo'q narsani o'chirib bo'lmidi!

# # pop bilan ishlash
# # 21-misol
# cars = ["BMW", "Mercedes", "Audi", "Lexus", "Toyota"]
# cars.pop(4)
# print(cars)
# # 22-misol
# laptops = ["Dell", "HP", "Asus", "Acer", "Apple"]
# laptops.pop(0)
# print(laptops)
# # 23-misol
# sonlar_royhati = ['1', '2', '3', '4', '5']
# sonlar_royhati.pop(2)
# print(sonlar_royhati)
# # 24-misol
# # tushunmadim
# # 25-misol
# index = int(input("indeksini kiriting: "))
# royhat = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# royhat.pop(index)
# print(f'Men hozir {royhat} dan')
# ochir = royhat.pop(index)
# print(f'{ochir} ni ochirdim!')