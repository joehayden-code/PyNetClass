dataList = [{'a': 1}, {'b': 3}, {'c': 5}]
index = 0
while index < len(dataList):
    for key in dataList[index]:
        print(dataList[index][key])
    index += 1
