import math
from texttable import Texttable
from collections import defaultdict
from operator import itemgetter

# File path
ratings_file = "C://Users/Jihui/Documents/Cpts315/HW2/ratings.csv"
# tags_file = "C://Users/Jihui/Documents/Cpts315/HW2/tags.csv"
# links_file = "C://Users/Jihui/Documents/Cpts315/HW2/links.csv"
movies_file = "C://Users/Jihui/Documents/Cpts315/HW2/movies.csv"

# read file and return rates list
def readFile(fileData):
    rates = []
    f = open(fileData, "r")
    data = f.readlines()
    f.close()
    line_num = 0
    for line in data:
        line_num += 1
        if (line_num != 1):
            dataLine = line.split(",")
            rates.append([int(dataLine[0]), float(dataLine[1]), float(dataLine[2])])
    return rates


# Create movie dictionary and user dictionary
# user：dic[user id]=[(movieId1,rating1),(movieId2,rating2)...]
# movie：dic[movie id]=[userId1,userId2...]
def createDict(rates):
    user_dict = {}
    movie_dict = {}
    for i in rates:
        if i[0] in user_dict:
            user_dict[i[0]].append((i[1], i[2]))
        else:
            user_dict[i[0]] = [(i[1], i[2])]
        if i[1] in movie_dict:
            movie_dict[i[1]].append(i[0])
        else:
            movie_dict[i[1]] = [i[0]]
    return user_dict, movie_dict


# Compute the similarity
def itemCF(user_dict):
    N = dict()
    C = defaultdict(defaultdict)
    W = defaultdict(defaultdict)
    for key in user_dict:
        for i in user_dict[key]:
            if i[0] not in N.keys():
                N[i[0]] = 0
            N[i[0]] += 1
            for j in user_dict[key]:
                if i == j:
                    continue
                if j not in C[i[0]].keys():
                    C[i[0]][j[0]] = 0
                C[i[0]][j[0]] += 1
    for i, related_item in C.items():
        for j, cij in related_item.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    return W


# Sort the top 5 interests item
def recommondation(user_id, user_dict, K):
    rank = defaultdict(int)
    l = list()
    W = itemCF(user_dict)
    for i, score in user_dict[user_id]:
        for j, wj in sorted(W[i].items(), key=itemgetter(1), reverse=True)[0:K]:
            if j in user_dict[user_id]:
                continue
            rank[j] += score * wj
    l = sorted(rank.items(), key=itemgetter(1), reverse=True)[0:5]
    return l

# Get movie list from movie.csv file
def getMovieList(item):
    items = {}
    f = open(item, encoding="utf_8")
    movie_content = f.readlines()
    f.close()
    line_num = 0
    for movie in movie_content:
        line_num += 1
        if (line_num != 1):
            movieLine = movie.split(",")
            items[int(movieLine[0])] = movieLine[1:]
    return items


# Main
if __name__ == '__main__':
    itemTemp = getMovieList(movies_file)  # Get movie list
    fileTemp = readFile(ratings_file)  # read file
    out = open("C://Users/Jihui/Documents/Cpts315/HW2/output.txt", 'w')
    user_dic, movie_dic = createDict(fileTemp)  # create a dic
    a = 1
    user_id = a
    for a in range(1, len(user_dic) + 1):
        user_id = a
        print(user_id)
        movieTemp = recommondation(user_id, user_dic, 100)  # sort the movies
        rows = []
        table = Texttable()  # Create the table and display it
        table.set_deco(Texttable.HEADER)
        rows.append([])

        for i in movieTemp:
            rows.append([user_id, itemTemp[i[0]][0]])
        table.add_rows(rows)
        print("%.3f" % (a / len(user_dic) * 100),
              "%")
        out.write(table.draw())
        a = a + 1
    else:
        print("Boom!")
    out.close()