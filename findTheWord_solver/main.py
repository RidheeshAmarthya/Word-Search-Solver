import numpy as np

#Row and Column size of the Word Search Matrix
row = 24
column = 24

#Prints the Word Search matrix with index
def printit(string2array):

    i = 0
    while (i != row * column):
        if (i % row == 0):
            print("\n")
        print(string2array[i], "%3.0f" % i, "", end='')
        i += 1

#Finds the words in Rows
def findRow(String, Find):

    index = String.find(Find)
    if index == -1:
        temp = String[::-1]
        index = temp.find(Find)
        a = []
        for i in range(row * column):
            a.append(row * column - i - 1)
        return a[index]
    else:
        return index

#Finds the words in Column
def findColumn(String, Find):

    arr = np.array([char for char in String])
    arr = arr.reshape(row, column)
    transpose = arr.copy()

    i = 0
    j = 0
    while i < row:
        while j < column:
            transpose[j][i] = arr[i][j]
            j += 1
        j = 0
        i += 1

    final = ''
    i = 0
    j = 0
    while i < row:
        while j < column:
            final = final + transpose[i][j]
            j += 1
        j = 0
        i += 1

    index = findRow(final, Find)

    a = np.arange(0, row * column)
    a = a.reshape(row, column)
    b = a.copy()

    i = 0
    j = 0
    while i < row:
        while j < column:
            b[j][i] = a[i][j]
            j += 1
        j = 0
        i += 1
    b = b.flatten()
    return(b[index])

#Find the words Diagonally
def findDiagonal(String, Find):

    charArr = [char for char in String]
    a = np.arange(row * column).reshape(row ,column)

    diag1 = [a[::, ::-1].diagonal(-i) for i in range(-a.shape[0] + 1, a.shape[1])] # [[0], [1, 3], [2, 4, 6], [5, 7], [8]]
    diag2 = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])] #  [[0], [3, 1], [6, 4, 2], [7, 5], [8]]
    diag3 = (a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1)) # [[2], [1, 5], [0, 4, 8], [3, 7], [6]]
    diag4 = (a.diagonal(-i) for i in range(a.shape[1] - 1, -a.shape[0], -1)) # [[6], [3, 7], [0, 4, 8], [1, 5], [2]]

    d1 = [n.tolist() for n in diag1]
    d2 = [n.tolist() for n in diag2]
    d3 = [n.tolist() for n in diag3]
    d4r = [n.tolist() for n in diag4]

    d4 = []
    for i in range(len(d4r)):
        for j in range(len(d4r[i])):
            d4.append(d4r[i][j])
    d4 = d4[::-1]

    d3r = []
    for i in range(len(d3)):
        for j in range(len(d3[i])):
            d3r.append(d3[i][j])
    d3 = d3r[::]

    d2r = []
    for i in range(len(d2)):
        for j in range(len(d2[i])):
            d2r.append(d2[i][j])
    d2 = d2r[::]

    d1r = []
    for i in range(len(d1)):
        for j in range(len(d1[i])):
            d1r.append(d1[i][j])
    d1 = d1r[::]

    final1 = ""
    i = 0
    while i < row * column:
        final1 = final1 + str(charArr[d1[i]])
        i += 1

    final2 = ""
    i = 0
    while i < row * column:
        final2 = final2 + str(charArr[d2[i]])
        i += 1

    final3 = ""
    i = 0
    while i < row * column:
        final3 = final3 + str(charArr[d3[i]])
        i += 1

    final4 = ""
    i = 0
    while i < row * column:
        final4 = final4 + str(charArr[d4[i]])
        i += 1

    index1 = findRow(final1, Find)
    index2 = findRow(final2, Find)
    index3 = findRow(final3, Find)
    index4 = findRow(final4, Find)

    if index1 > 0:
        return d1[index1]
    if index2 > 0:
        return d2[index2]
    if index3 > 0:
        return d3[index3]
    if index4 > 0:
        return d4[index4]
    else:
        return 0

#Main Function
def main():

    words = 15
    i = 0

    arrayString_input = "UDIMJAYMFGWAZMMSXOWYJJKQIUYYLBMESSALANOITANSXCRRDANVTKECCHNOELOPANGXQCOXYYRVBWTPBVYDYGELYNMUFEBOFKFOAZTLYQIRWAUOLDXJBBEILLKXKTEWEHUBMHXIFJPIAUSCGHYZYBNQSGIAWHGYLLJSHRPPCUTVBPILTNFKACUGYLTNFOIZEPJZBROWAFAXCXYYAIOGPVEJKEFUTXTRTQPLNEGULTLTKGRWLYIVHBNFEYTLPVSLTTTXIARKCLINFRAPSUTIVTEYWLYTKNEEJGAENJEEGSJCRSTKEYTFQTEITYEPUEIREPZIVRKXWRIZHYKVOEJCRCRRNXAAZEGDCNLQVENXNGUALIAWENCMINFFPWIXAIESYTRPZEMHRSUZUOTHRWBJSMBIOPTNPTRKAJBWOMSYIAOHIHUUMDZQDMDGLFLLQMRANMNGDJJORSOULOLMYUBQXOUBTXECDDILFSGGIDGRMUPDQCRCIROTESBMJREIGNOFTERRORRJDRERSUSDOKGCGPOWJTZRDSTLUYCBZKBKFBDJDUYSYIATDCOSNXMLWWWR"
    string2array = [char for char in arrayString_input]

    arrayString_input_words = "OLDREGIME NAPOLEON AUSTRIA FRANCE BASTILLE ESTATESGENERAL COMMONERS NOBILITY CLERGY REIGNOFTERROR NATIONALASSEMBLY MARIEANTOINETTE LOUISXVI ROBESPIERRE GUILLOTINE"
    string2array_words = arrayString_input_words.split()

    print(string2array_words)
    printit(string2array)
    print('\n')

    while i < words:
        if findRow(arrayString_input, string2array_words[i]) != 0:
            print("Row:      ", "%3.0f" % findRow(arrayString_input, string2array_words[i]), i, string2array_words[i])
        if findColumn(arrayString_input, string2array_words[i]) != 0:
            print("Column:   ", "%3.0f" % findColumn(arrayString_input, string2array_words[i]), i, string2array_words[i])
        if findDiagonal(arrayString_input, string2array_words[i]) != 0:
            print("Diagonal: ", "%3.0f" % findDiagonal(arrayString_input, string2array_words[i]), i, string2array_words[i])
        i += 1

#Main function call
main()