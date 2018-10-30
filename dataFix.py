import csv

with open("fer2013_reformatted.csv", 'wt') as writeFile:
    writer = csv.writer(writeFile)
    with open("fer2013.csv", 'rt') as file:
        reader = csv.reader(file)
        rownum = 0
        for row in reader:
            if rownum != 0:
                add = []
                add.append(row[0])
                # give each pixel value its own column
                splitstring = row[1].split()
                add.extend(splitstring)
                # 0 - training, 1 - PublicTest, 2 - PrivateTest
                usage = row[2]
                if usage == 'Training':
                    add.append(0)
                elif usage == 'PublicTest':
                    add.append(1)
                elif usage == 'PrivateTest':
                    add.append(2)
                else:
                    raise Exception ('Bad usage')
                writer.writerow(add)
            else:
                rownum = rownum + 1

