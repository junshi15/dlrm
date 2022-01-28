import csv

infilename = 'train.txt'
outfilename = 'train_uid.csv'
n = 100000

rows = []
with open(infilename, newline='') as infile, open(outfilename, 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter='\t')
    writer = csv.writer(outfile, delimiter='\t')
    for idx, row in enumerate(reader):
        if idx % n == 0:
            print(f'at line {idx}')
            if rows:
                writer.writerows(rows)
                rows = []
        rows.append(row + [idx])
    if rows:
        writer.writerows(rows)

