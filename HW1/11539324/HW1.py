"""
jihui.sheng
11539324
HW1
"""
import itertools
#IN_FILE="C://Users/Jihui/Documents/Cpts315/HW1/11539324/browsing-data.txt"
IN_FILE = "C://Users/Jihui/Documents/Cpts315/HW1/browsingdata_50baskets.txt"
#OUT_FILE ="C://Users/Jihui/Documents/Cpts315/HW1/11539324/output.txt"
OUT_FILE ="C://Users/Jihui/Documents/Cpts315/HW1/output.txt"

#Open the input file for reading
with open(IN_FILE, "r") as file_name:
    all_lines = file_name.readlines()
file_name.close()

#The first filter to get the 1-item frequent in dictionary
def filter_1():
    whole_words = []
    for i in all_lines:
        lines = i.split()
        for j in lines:
            words = j.split()
            str1 = ''.join([str(x) for x in words])
            #str2 = re.sub("[A-Za-z\!\%\[\]\,\。]", "", str1)
            whole_words.append(str1)

    #print(whole_words)
    dic = {}
    for k in whole_words:
        if(k in dic):
            dic[k] += 1
        else:
            dic[k] = 1
    #print(dic)
    return filter(dic)

#The filter function for get the frequent items which >=100
def filter(data):
    #return {key: value for key, value in data.items() if value >= 100}
    return {key: value for key, value in data.items() if value >= 8}

#To get the 2-items frequent list
def get_list_1():
    dic_1 = filter_1()
    list_2 = []
    list_3 = []
    key = list(dic_1.keys())
    for k in range(len(key)):
        for j in range(k+1,len(key)):
            list_2 = sorted([key[k],key[j]])
            list_3.append(list_2)
                    
    #print(list_3)
    return list_3

#The second filter to get the 2-items frequent in dictionary
def filter_2():
    list_4 = get_list_1()
    list_5 = []
    list_6 = []
    dic_2 = {}
    for i in all_lines:
        lines = i.split()
        list_5.append(lines)
    #print(list_5)
    for j in range(len(list_4)):
        for k in range(len(list_5)):
            if((list_4[j][0] in list_5[k]) and (list_4[j][1] in list_5[k])):
                if(list_4[j][0] != list_4[j][1]):
                    list_6.append([list_4[j][0],list_4[j][1]])
            else:
                continue

    for item in list_6:
        s = str(item)
        if s in dic_2.keys():
            dic_2[s] += 1
        else:
            dic_2[s] = 1
    dic_3 = {}
    dic_3 = filter(dic_2)
 
    #for key in dic_3.keys():
        #print('%s is %d' % (key, dic_3[key]))
    #print(dic_3)
    return dic_3

#The third filter to get the 3-items frequent in dictionary
def filter_3():
    dic_4 = filter_2()
    list_7 = []
    list_8 = []
    list_9 = []
    list_10 = []
    list_11 = []
    list_12 = []
    dic_5 = {}
    key = list(dic_4.keys())
    for k in range(len(key)):
        list_7.append(eval(key[k]))

    for i in range(len(list_7)):
        list_8.append(list_7[i][0])
        list_8.append(list_7[i][1])
   
    for j in list_8:
        if j not in list_9:
            list_9.append(j)
    #print(list_9)

    for a in all_lines:
        lines = a.split()
        list_10.append(lines)

    for x in range(len(list_9)):
        for y in range(x+1,len(list_9)):
            for z in range(y+1,len(list_9)):
                list_11.append([list_9[x],list_9[y],list_9[z]])
    for b in range(len(list_11)):
        for c in range(len(list_10)):
            if((list_11[b][0] in list_10[c]) and (list_11[b][1] in list_10[c]) and (list_11[b][2] in list_10[c])):
                if(list_11[b][0] != list_11[b][1]) and (list_11[b][1] != list_11[b][2]) and (list_11[b][0] != list_11[b][2]):
                    list_12.append([list_11[b][0],list_11[b][1],list_11[b][2]])
            else:
                continue

    for item in list_12:
        s = str(item)
        if s in dic_5.keys():
            dic_5[s] += 1
        else:
            dic_5[s] = 1
    #print(filter_1(dic_5))
    return filter(dic_5)

#Calculate the percentage and sort the list
def calculate(data):
    for i in data:
        data[i] = data[i] / len(all_lines)
    dic_6 = sorted(data.items(),key=lambda data:data[1],reverse = True)
    """
    k = 1
    for j in dic_6:
        s = str(j[0]).strip('[]').replace('\'','').replace(',','')
        if(k <= 4):
            k += 1
            print(s,j[1])"""
    #print(dic_6)
    #dic_7 = list(dic_6)[:4]
    ##print(dic_6)
    return dic_6

# Open the output file for writing the first four frequent items
with open(OUT_FILE, "w") as text_file:
    text_file.write("OUTPUT A\n")
    for i in calculate(filter_2())[:4]:
        text_file.write(str(i).strip('()').replace('\"','').replace('[','').replace(']','').replace('\'','').replace(',','') + "\n")
    text_file.write("OUTPUT B\n")
    for j in calculate(filter_3())[:4]:
        text_file.write(str(j).strip('()').replace('\"','').replace('[','').replace(']','').replace('\'','').replace(',','') + "\n")
text_file.close()
#if __name__ == '__main__':
    #print(filter_1())
    #filter_1()
    #print(filter_2())
    #print(filter_3())
    #calculate(filter_1())
    #calculate(filter_2())
    #calculate(filter_3())
