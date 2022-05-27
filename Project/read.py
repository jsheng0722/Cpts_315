

def get_products():
    dic = {}
    aList = []
    with open('./order_products__prior.txt', 'r',encoding='utf-8') as file:
        f = file.readlines()
        for line in f:
            data = line.replace(',',' ').split()
            if data[0] not in aList:
                aList.append(data[0])
                dic[data[0]] = [data[1]]
            else:
                bList = dic[data[0]]
                bList.append(data[1])
                dic[data[0]] = bList

    with open('./order_p.txt', 'a+', encoding='utf-8') as file1:
        for i in dic:
            for j in dic[i]:
                file1.write(j + ' ')
            file1.write('\n')

