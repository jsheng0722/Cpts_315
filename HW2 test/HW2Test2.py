import csv

ratings_file = "C://Users/Jihui/Documents/Cpts315/HW2/ratings.csv"
def readfile(fName):
    rates = []
    line_num = 0
    with open(fName) as input_file:
        lines = input_file.readlines()
        for row in lines:
            line_num += 1
            if (line_num != 1):
                data = row.split(",")
                rates.append([(data[0]),(data[1]),(data[2])])
    print(rates)
    return rates

        
if __name__=='__main__':
    itemTemp = readfile(ratings_file)
