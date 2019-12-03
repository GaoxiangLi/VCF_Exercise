import re


def vcfread(filename):
    headers = []  # for header begin with #(## included)
    data = []  # for data
    with open(filename) as fh:
        # read file line by line
        for line in fh:
            if line.startswith('#'):
                # save headers alone
                headers.append(line)
            else:
                # what we need to operate and split by ';' '\n' '\t' ,  and put them into a multi_dimension array
                # use regular expression
                line = re.split(';|\t|\n', line)
                data.append(line)  # save to a list
        return headers, data

    # print(filename)
