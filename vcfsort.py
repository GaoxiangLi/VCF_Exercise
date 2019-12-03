import vcfreader


def sort(filename, key, order, saved_path):
    headers, data = vcfreader.vcfread(filename)
    # x : num of rows
    # str_1: prefix of key like 'AF='
    x = len(data)
    str_1 = key + '='

    # # loop to trace the key we want in each line
    # # find target column j
    # # get the target key value number and insert to head position
    for i in range(x):
        flag = 0
        for j in range(6, len(data[i]) - 1):  # ignore first 7 column
            if data[i][j].startswith(str_1):  # locate the key
                num = data[i][j].replace(str_1, '')  # use '' to replace prefix then can get key value
                if num != '.':  # some value is '.', convert string key value to float to sort
                    num = float(num)
                    data[i].insert(0, num)
                else:
                    data[i].insert(0, 0.0)  # Use 0 to replace "."
                flag = 1
                break
        #         since we need to sort the value, we must use a float number to replace "."
        #         use 0 maybe not a good solution, still need more work to feed a good solution
        if flag == 0:  # to check if key is missing
            data[i].insert(0, 0)

    # SORT
    # Timsort is used: Timsort is a hybrid stable sorting algorithm, derived from merge sort and insertion sort,
    # designed to perform well on many kinds of real-world data.

    # sort the head column
    data = sorted(data, key=lambda k: k[0], reverse=order)

    # delete duplicate first column after sorting
    for i in range(x):
        data[i].pop(0)

    # recover
    # connect to vcf format
    result = ''
    for i in range(x):
        for j in range(0, 7):  # first 7 columns delimiter as \t
            result += str(data[i][j])
            result += '\t'
        for j in range(7, len(data[i]) - 3):  # info column delimiter as ;
            result += data[i][j] + ';'
        for j in range(len(data[i]) - 3, len(data[i]) - 1):  # two columns after info, delimiter as \t
            result += '\t' + data[i][j]
        result += '\n'
    print('finished!')

    # save to file
    saved_path += 'SortBy'
    saved_path += key
    saved_path += '.vcf'
    f = open(saved_path, 'w')
    str1 = ''.join(headers)
    f.write(str1)  # headers
    f.write(result)  # data
    f.close()
    print('file saved at' + saved_path)
