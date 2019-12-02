import re


def vcfread(filename):
    headers = []
    data = []
    with open(filename) as fh:
        # read file line by line
        for line in fh:
            if line.startswith('#'):
                # save headers alone
                headers.append(line)
            else:
                # what we need to operate and split by ; \n \t ,  and put them into a multi_dimension array
                line = re.split(';|\t|\n', line)
                data.append(line)
        return headers, data

    # print(filename)
