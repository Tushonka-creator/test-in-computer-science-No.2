#Тушин Иван Константинович, сложность B, группа ИИ-72
x = 0
numbs = []
positive_numbs = 0
negative_numbs = 0
a = 1
while a == 1:
    try:
        numbs.append(int(input("введите числа, чтобы закончить ввод чисел напишите стоп")))
    except ValueError:
        while a == 1:
            try:
                if numbs[x]<0:
                    negative_numbs = negative_numbs + 1
                    x = x+1
                elif numbs[x]>0:
                    positive_numbs = positive_numbs+1
                    x = x+1
            except IndexError:
                    print(positive_numbs)
                    print(negative_numbs)
    print(' ')
