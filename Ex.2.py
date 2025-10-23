#Тушин Иван Константинович, сложность B, группа ИИ-72
x = 0
numbs = []
positive_numbs = 0
negative_numbs = 0
a = 0
b = 1
while b == 1:
    try:
        numbs.append(int(input("введите числа, чтобы закончить ввод чисел напишите стоп")))
    except ValueError:
        while a == x:
            if numbs[x]<0:
                negative_numbs = negative_numbs + 1
                x = x+1
                a = a+1
            elif numbs[x]>0:
                positive_numbs = positive_numbs+1
                x = x+1
                a = a+1
print(positive_numbs)
print(negative_numbs)