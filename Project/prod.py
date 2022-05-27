
def final_p():
    dic_pro = {}
    a = []
    b = []
    with open('products.txt','r',encoding='utf-8') as file:
        f = file.readlines()
        for line in f:
            data = line.split(',')
            dic_pro[data[0]] = data[1]
    with open('10top_2produts.txt','r',encoding='utf-8') as file2:
        f = file2.readlines()
        for line in f:
            data = line.split()
            a.append(dic_pro[data[0]])
            b.append(dic_pro[data[1]])

    with open('10top_2p.txt','w',encoding='utf-8') as file3:
        for i in range(len(a)):
            file3.write(str(a[i].replace('\n','')) + ',' + str(b[i]))

    file.close()
    file2.close()
    file3.close()


if __name__ == '__main__':
    final_p()