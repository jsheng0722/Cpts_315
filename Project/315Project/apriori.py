# Hongqi.guo & Jihui.Sheng
NUM_SUP = 500
def read_data(filename):
    print('loading data... ', end='')
    browsing_session = []                               # read the line in data put in list
    with open(filename, 'r') as f:
        for line in f.readlines():
            items = set(line.strip().split())
            browsing_session.append(items)
    print('done')
    return browsing_session


def create_single_item_set(browsing_session):
    print('creating single item set... ', end='')
    single_item_set = set()
    for session in browsing_session:
        for item in session:
            single_item_set.add(item)
    print('done')
    return single_item_set


def create_single_item_support(browsing_session):
    print('creating single item support... ', end='')
    statistics = {}
    single_item_support = {}
    for session in browsing_session:
        for item in session:
            if item not in statistics:
                statistics[item] = 0
            statistics[item] += 1
    for item, count in statistics.items():
        if count >= NUM_SUP:
            score = count / len(browsing_session)
            single_item_support[item] = score
    print('done')
    return single_item_support


def create_pairs_item_set(single_item_support):
    print('creating pairs item set... ', end='')
    pairs_item_set = set()
    single_item_support_list = list(single_item_support)
    for i in range(len(single_item_support_list)):
        for j in range(i, len(single_item_support_list)):
            item1 = single_item_support_list[i]
            item2 = single_item_support_list[j]
            if item1 < item2:
                pairs_item_set.add((item1, item2))
            elif item1 > item2:
                pairs_item_set.add((item2, item1))
    print('done')
    return pairs_item_set


def create_pairs_item_support(browsing_session, pairs_item_set):
    print('creating pairs item support... ', end='')
    statistics = {}
    pairs_item_support = {}
    i = 0
    for session in browsing_session:
        i += 1
        if i % 100 == 0:
            print('{:.2f}%'.format(i / len(browsing_session) * 100))
        for item in pairs_item_set:
            if item[0] in session and item[1] in session:
                if item not in statistics:
                    statistics[item] = 0
                statistics[item] += 1
    for item, count in statistics.items():
        if count >= NUM_SUP:
            pairs_item_support[item] = count / len(browsing_session)
    print('done')
    return pairs_item_support


def compute_confidence_scores_for_pairs_item(single_item_support, pairs_item_support):
    print('computing confidence scores for pairs item... ', end='')
    confidence_scores = {}
    for pair, score in pairs_item_support.items():
        item0 = pair[0]
        item1 = pair[1]
        confidence_score0 = score / single_item_support[item0]
        confidence_score1 = score / single_item_support[item1]
        confidence_scores[item0 + ' ' + item1] = confidence_score0
        confidence_scores[item1 + ' ' + item0] = confidence_score1
    print('done')
    return confidence_scores

def calculate_top_10_confidence_scores(confidence_scores):
    items = []
    scores = []
    for _, score in confidence_scores.items():
        scores.append(score)
    scores.sort(reverse=True)
    keys = set(confidence_scores.keys())
    for item in keys:
        if confidence_scores[item] >= scores[9]:
            items.append((item, confidence_scores[item]))
    items.sort(key=lambda s:(-s[1], s[0]))
    if len(items) >= 10:
        items = items[0:10]
    return items

def get_products_in_order():
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

    with open('./order_p.txt', 'w', encoding='utf-8') as file1:
        for i in dic:
            for j in dic[i]:
                file1.write(j + ' ')
            file1.write('\n')
    file.close()
    file1.close()

# get the buying time from each order
def read_order_time():
    dic_ot = {}
    with open('./orders.txt', 'r') as file:
        f = file.readlines()
        for line in f:
            data = line.replace(',', ' ').split()
            dic_ot[str(data[0])] = data[1]
    # print('dic_ot is : ' + str(dic_ot) + "\n")
    file.close()
    return dic_ot

def freq_getOrder():
    a = []
    b = []
    aList = []
    dic = {}
    dic1 = {}
    with open('./10top_2produts.txt', 'r') as file:
        f = file.readlines()
        for line in f:
            data = line.split()
            a.append(data[0])                   # get the first value
            b.append(data[1])                   # get the second value, put them into list

    with open('./order_products__prior.txt', 'r', encoding='utf-8') as file1:
        f = file1.readlines()
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
    with open('./orders_in_t.txt', 'w', encoding='utf-8') as file2:
        for i in dic1:
            for j in dic1[i]:
                if j in dic_ot:
                    file2.write(dic_ot[j] + ' ')
                else:
                    pass
            file2.write('\n')

    # print("dic is: " + str(dic) + "\n")
    # print("dic1 is: " + str(dic1) + "\n")
    file.close()
    file1.close()
    file2.close()

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

def count_top_time():
    a = []
    b = []
    m = []
    with open('./orders_in_t.txt','r') as file:
        f = file.readlines()
        for line in f:
            data = line.split()
            dic_topt = {}
            for i in data:
                if i not in dic_topt:
                    dic_topt[i] = 1
                else:
                    dic_topt[i] += 1
            m.append(max(dic_topt,key=dic_topt.get))
    print("list of max time is: " + str(m) + '\n')
    with open('./10top_2p.txt', 'r') as file1:
        f = file1.readlines()
        for line in f:
            data = line.split(',')
            a.append(data[0])                   # get the first value
            b.append(data[1])                   # get the second value, put them into list
    with open('./the_max_time_buy.txt','w') as file2:
        for i in range(len(m)):
            file2.write(str(a[i].replace('\n','')) + "," + str(b[i].replace('\n','')) + ": " + str(m[i]) + '\n')
            print(str(a[i].replace('\n','')) + " and " + str(b[i].replace('\n','')) + "are better sell in: (" + str(m[i]) + ":00)" + '\n')
    file.close()
    file1.close()
    file2.close()

if __name__ == '__main__':
    file = './order_p.txt'
    browsing_session = read_data(file)
    
    single_item_set = create_single_item_set(browsing_session)
    single_item_support = create_single_item_support(browsing_session)
    
    pairs_item_set = create_pairs_item_set(single_item_support)
    pairs_item_support = create_pairs_item_support(browsing_session, pairs_item_set)
    
    confidence_score = compute_confidence_scores_for_pairs_item(single_item_support, pairs_item_support)
    top_10_confidence_score = calculate_top_10_confidence_scores(confidence_score)
    out = open('./10top_2produts.txt', 'w')
    # out.write('OUTPUT A\n')
    for item in top_10_confidence_score:
        print('{} {:.4f}'.format(item[0], item[1]))
        out.write('{} {:.4f}\n'.format(item[0], item[1]))
    #close file
    out.close()

    # list the each order products
    get_products_in_order()

    # get order time list
    freq_getOrder()

    # get 10top fre items name
    final_p()

    # calculate the freq time that order placed
    count_top_time()
