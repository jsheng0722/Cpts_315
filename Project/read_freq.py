





def read_order_time():
    dic_ot = {}
    with open('./orders.txt', 'r') as file:
        f = file.readlines()
        for line in f:
            data = line.replace(',', ' ').split()
            dic_ot[str(data[0])] = data[1]
    return dic_ot

def freq_getOrder():
    a = []
    b = []
    aList = []
    dic = {}
    dic1 = {}
    dic_ot = {}
    with open('./10top_2produts.txt', 'r') as file:
        f = file.readlines()
        for line in f:
            data = line.split()
            a.append(data[0])                   # get the first value
            b.append(data[1])                   # get the second value, put them into list

    with open('./order_products__prior.txt', 'r', encoding='utf-8') as file:
        f = file.readlines()
        for line in f:
            data = line.replace(',', ' ').split()
            if data[0] not in aList:
                aList.append(data[0])
                dic[data[0]] = [data[1]]
            else:
                bList = dic[data[0]]
                bList.append(data[1])
                dic[data[0]] = bList
    # dic is {order1: [item1,item2,...],order2:[item1,item2,...]...}

    # start froem i = 0, use the first group value
    for i in range(len(a)):
        c = str(a[i]) + ' ' + str(b[i])
        cList = []
        #search from dic
        for x in dic:
            # if a[i] and b[i] both in values()
            if a[i] in dic[x]:
                if b[i] in dic[x]:
                    #add order list in this group
                    cList.append(x)
                    dic1[c] = cList
    dic_ot = read_order_time()
    with open('./orders_in_t.txt', 'w', encoding='utf-8') as file1:
        for i in dic1:
            for j in dic1[i]:
                if j in dic_ot:
                    file1.write(dic_ot[j] + ' ')
                else:
                    pass
            file1.write('\n')


def count_top_time():
    a = []
    b = []
    m = []
    with open('./orders_in_t.txt','r') as file2:
        f = file2.readlines()
        for line in f:
            data = line.split()
            dic_topt = {}
            for i in data:
                if i not in dic_topt:
                    dic_topt[i] = 1
                else:
                    dic_topt[i] += 1
            m.append(max(dic_topt,key=dic_topt.get))
    with open('./10top_2produts.txt', 'r') as file:
        f = file.readlines()
        for line in f:
            data = line.split()
            a.append(data[0])                   # get the first value
            b.append(data[1])                   # get the second value, put them into list
    with open('./the_max_time_buy.txt','w') as file3:
        for i in range(len(m)):
            file3.write(str(a[i]) + " " + str(b[i]) + ": " + str(m[i]) + '\n')


if __name__ == '__main__':
    # read_order_time()
    # freq_getOrder()
    count_top_time()
    # result = get_order_freq_time('28204 24852')
    # print(result)
