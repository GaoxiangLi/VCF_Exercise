import vcfreader


def sort(filename, key, order, saved_path):
    headers, data = vcfreader.vcfread(filename)

    # # loop to trace the key we want in each line
    x = len(data)
    str_1 = key + '='

    # # find target column j
    # # get the target number and insert to head
    for i in range(x):
        flag = 0
        for j in range(6, len(data[i]) - 1):
            if data[i][j].startswith(str_1):
                num = data[i][j].replace(str_1, '')
                if num != '.':
                    num = float(num)
                    data[i].insert(0, num)
                else:
                    data[i].insert(0, 0.0)
                flag = 1
                break
        if flag == 0:  # to check if key is missing
            data[i].insert(0, 0)

    # SORT
    # Timsort is used: Timsort is a hybrid stable sorting algorithm, derived from merge sort and insertion sort,
    # designed to perform well on many kinds of real-world data.
    data = sorted(data, key=lambda k: k[0], reverse=order)

    # delete duplicate column
    for i in range(x):
        data[i].pop(0)

    # recover
    # connect to vcf format
    result = ''
    for i in range(x):
        for j in range(0, 7):
            result += str(data[i][j])
            result += '\t'
        for j in range(7, len(data[i]) - 3):
            result += data[i][j] + ';'
        for j in range(len(data[i]) - 3, len(data[i]) - 1):
            result += '\t' + data[i][j]
        result += '\n'
    print('finished!')
    # save to file
    saved_path += 'SortBy'
    saved_path += key
    saved_path += '.vcf'
    f = open(saved_path, 'w')
    str1 = ''.join(headers)
    f.write(str1)
    f.write(result)
    f.close()
    print('file saved at' + saved_path)
