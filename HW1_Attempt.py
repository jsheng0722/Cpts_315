"""
    read file 1
"""
def read_baskert():
    baskets_list = []
    with open("browsingdata.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        baskets_list .append(line.split())
    retrun baskets_list

"""
    read file 2
"""
import csv
def read_baskets_II(fname):
        record = []
        with open(fname) as input file:
            lines = csv.reader(input_file, delimiter = ' ')
            for row in lines:
                record.append(row[:-1])
        return record
"""
    count the item and put into dictionary
"""
def init_C1(baskets_list):
    item_dict = {}
    for basket in baskets_list:
        for item in basket:
            if item not in item_dict:
                item_dict[item] = 1
            else:
                item_dict[item] += 1
    return item_dict

def init_L1(item_dict, support = 100):
    L1 = {}
    for key, value in item_dict.items():
        if value >= support:
            L1[key] = value
    return L1

def init_L1_II(baskets_list, support = 100):
    counter_dict = collections.Counter()
    for basket in baskets_list:
        for item in basket:
            counter_dict[item] += 1

    L1 = {i:counter_dict[i] for i in counter_dict if counter_dict[i] >= support}
    return L1

import numpy as np
def gaussian_neihbour(a):
    mu, sigma = 0, 1
    noise = np.random.normal(mu, sigma, 1)[0]
    return a + noise

#gaus_neighbours = [gaussian_neighbour(s) for _ in range(20)]

def generateLk(Lk_1, baskets_list, k, support = 100):
    set_of_keys = []
    a = 0
    for key, _ in Lk_1.items():
        if type(key) == tuple:
            for elem in key:
                if elem not in set_of_keys:
                    set_of_keys.append(elem)
        else:
            if key not in set_of_keys:
                set_of_keys.append(key)
    Lk = {}
    for item in itertools.combinations(set_of_keys, k):
        Lk[tuple(sorted(item))] = 0
    for basket in baskets_list:
        basket = sorted(basket)
        combs_iterator = itertools.collections(basket, k)
        for combs in combs_iterator:
            if combs in Lk.keys():
                Lk[combs] += 1
    Lk = {i: Lk[i] for i in Lk if Lk[i] >= support}
    return Lk

    def generateLk_II(baskets_list, k, support = 100):
        counter_dict = collections.Counter()
        for basket in baskets_list:
            basket = sorted(basket)
            combs_iterator = itertools.collections(basket, k)
            for combs in combs_iterator:
                counter_dict[combs] += 1
        Lk = {i: counter_dict[i] for i in counter_dict if counter_dict[i] >= support}
        return Lk

def top_k_sorted_dict(dict_, k):
    s_dict = list(sorted(dict_.items, key = lambda item: item[1]))
    return s_dict[(-1-k):-1]

def confidenceScore_k(Lk, Lk_1, k, k_top = 5):
    temp = {}
    conf_score = collections.Counter()
    if k > 2:
        for x in Lk_1:
            Lk_1[tuple(sorted(x))] = Lk_1[x]
        for x in Lk:
            x = tuple(sorted(x))
            tuple_rotator = collections.deque(x)
            for _ in range(k):
                tp1 = tuple(tuple_ratator)
                tp1 = tuple(sorted(tp1[:-1]))+(tp1[-1],)
                temp[tp1] = Lk[x]
                tuple_rotator.rotate()
        for elem in temp:
            if k == 2:
                conf_score[elem] = temp[elem] / float(Lk_1[elem[0]])
            else:
                conf_score[elem] = temp[elem] / float(Lk_1[elem[:-1]])
        return top_k_sorted_dict(conf_score, k_top)