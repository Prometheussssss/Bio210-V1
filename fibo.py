fibo_list = list([0, 1])

for i in range(48) :

    F0 = fibo_list[i]

    F1 = fibo_list[i+1]

    F2 = F0 + F1

    fibo_list.append(F2)