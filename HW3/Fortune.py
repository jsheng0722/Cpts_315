from sklearn.datasets import load_digits
from sklearn.linear_model import perceptron, Perceptron
from numpy import dot,sign

# read file
def read_file(newFile):
    fp = open(newFile, 'r')
    data = fp.read().splitlines()
    fp.close()
    return data

# get the words list
def get_words_except_stopW(file1,file2):
    aList = []
    for datas in file1:
        data = datas.split()
        for words in data:
            if words not in aList:
                aList.append(words)
    for words in file2:
        if words in aList:
            aList.remove(words)
    return (sorted(aList))

#
def getData(file):
    i = 0
    for datas in file:
        data = datas.split()
        for words in stop_list:
            for word in data:
                if (word == words):
                    data.remove(word)
        newData = sorted(data)
        file[i] = ' '.join(newData)
        i += 1
    return file

def getVec(file,li):
    v = []
    for i in range(0, len(file)):
        bList = []
        for j in range(0, len(li)):
            bList.append(0)
        v.append(bList)
    return v

def get_fortune(file,li,v):
    file = getData(file)
    i = 0
    for datas in getData(file):
        data = datas.split()
        for word in data:
            index = li.index(word)
            v[i][index] = 1
        i += 1
    return v

# change '0' labels to '1'
def change_labels(labelFile):
    for x in range(0, len(labelFile)):
        if (labelFile[x] == '0'):
            labelFile[x] = '-1'
    return labelFile

def calcul(file1,file2, v):
    T = 20
    w = []
    acc = []
    mstk_l = []
    label = change_labels(file2)

    #Initialize the weights w = 0: [0,0,0,.....]
    for x in range(0, len(get_words_except_stopW(file1,stop_list))):
        w.append(0)

    #for each training iteration itr ∈ {1, 2, · · ·, T} do
    for i in range(1, T+1):
        mstk = 0
        # for each training example (xt, yt) ∈ D do
        for j in range(0, len(file1)):
            Xt = v[j]
            Yt = int(label[j])
            # yˆt = sign(w · xt) // predict using the current weights
            y = sign(dot(w, Xt))
            # if mistake then
            if (y != Yt):
                w0 = [x * Yt for x in Xt]
                # w = w + η · yt · xt // (η = 1), update the weights
                w = [x + y for x, y in zip(w, w0)]
                mstk = mstk + 1
            else:
                pass

        acc.append((len(file1) - mstk) / len(file1))
        mstk_l.append(mstk)
        # # a) Compute the the number of mistakes made during each iteration (1 to 20)
        # print("iteration-" + str(i) + " no-of-mistakes: " + str(mstk_l[i-1]))
        # # b) Compute the training accuracy and testing accuracy after each iteration(1 to 20).
        # if(file1 == train_data):
        #     print("iteration-" + str(i) + " training-accuracy: " + str(acc[i-1]))
        # elif(file1 == test_data):
        #     print("iteration-" + str(i) + " Testing-accuracy: " + str(acc[i-1]))
        # else:
        #     print("No file can found")
        return acc,mstk_l


if __name__ == "__main__":
    # read file
    train_data = read_file('traindata.txt')
    train_labels = read_file('trainlabels.txt')
    stop_list = read_file('stoplist.txt')
    test_data = read_file('testdata.txt')
    test_labels = read_file('testlabels.txt')

    mData = get_words_except_stopW(train_data, stop_list)
    # print(mData)
    mTData = get_words_except_stopW(test_data, stop_list)
    # print(mTData)
    nData = getData(train_data)
    # print(nData)
    nTData = getData(test_data)
    # print(nTData)
    vec = getVec(nData,mData)
    # print(vec)
    vecT = getVec(nTData,mData)
    # print(vecT)
    fortune = get_fortune(nData,mData,vec)
    # print(fortune)
    fortuneT = get_fortune(nTData,mTData,vecT)
    # print(fortuneT)

    acc_train,mist = calcul(nData,train_labels,fortune)
    acc_test,mist = calcul(nTData,test_labels,fortuneT)

    # c) Compute the training accuracy and testing accuracy after 20 iterations with standard perceptron and averaged perceptron.
    X, y = load_digits(return_X_y=True)
    clf = Perceptron(tol=1e-3, random_state=0)
    clf.fit(X, y)
    Perceptron()
    clf.score(X, y)
    # print(clf.score(X, y))
    with open('output.txt','a') as file_handle:
        for j in mist:
            file_handle.write("iteration-" + str(j+1) + " no-of-mistakes:" + str(mist[j]))
        for i in acc_train:
            file_handle.write("iteration-" + str(i+1) + " training-accuracy:" + str(acc_train[i]))
        for i in acc_test:
            file_handle.write(" testing-accuracy: " + str(acc_test[i]))
        #training-accuracy-standard-perceptron training-accuracy-averaged-perceptron
        file_handle.write("training-accuracy-standard-perceptron is: " + str(clf.score(X, y)))
        #testing-accuracy-standard-perceptron testing-accuracy-averaged-perceptron
        file_handle.write('\n')
