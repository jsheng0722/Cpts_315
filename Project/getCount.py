
a =[]
with open('./orders_in_t.txt', 'r') as file:
    f = file.readlines()
    for line in f:
        data = line.split()
        dic_topt = {}
        for i in data:
            if i not in dic_topt:
                dic_topt[i] = 1
            else:
                dic_topt[i] += 1
        a.append(sorted(dic_topt.items(),key=lambda d:d[0]))
file.close()
with open("./countOfT.txt", 'w') as file1:
    for i in range(len(a)):
        file1.write(str(a[i]) + '\n')
file1.close()