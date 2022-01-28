import csv
import fastavro
import json
import numpy as np
from schema import SCHEMA

infilename = 'train_uid.csv'
outfilename = 'train_uid.avro'
infilename = '../../../test_dlrm/train_tiny.csv'
outfilename = '../../../test_dlrm/train_tiny.avro'
int_feat_start = 1
int_feat_end = 13
cat_feat_start = 14
cat_feat_end = 39
entity_idx = 20

n = 100000

rows = []
avro_schema = fastavro.parse_schema(json.loads(SCHEMA))
with open(infilename, newline='') as infile:
    reader = csv.reader(infile, delimiter='\t')
    records = []
    first = True
    f = None
    for idx, row in enumerate(reader):
        if row[entity_idx]:
            record = {'response': 0, 'entityId': str(row[entity_idx]), 'uid': None, 'perEntity': []}
        else:
            continue
        for j, feat in enumerate(row):
            if j == 0:
                record['response'] = int(feat)
            elif j == entity_idx:
                continue
            elif j == 40:
                record['uid'] = int(feat)
            elif j < cat_feat_start:
                if feat and int(feat) > 0:
                    ntv = {'name': 'dense', 'term': str(j), 'value': np.log(float(feat) + 1.0)}
                    record['perEntity'].append(ntv)
            elif feat:
                ntv = {'name': f'cat{j}', 'term': feat, 'value': 1.0}
                record['perEntity'].append(ntv)
        records.append(record)
        if idx % n == 0:
            print(f'at line {idx}')
            if records:  # dump the data to avro
                if first:
                    with open(outfilename, 'wb') as f0:
                        fastavro.writer(f0, avro_schema, records)
                    f = open(outfilename, 'ab+')
                    first = False
                else:
                    fastavro.writer(f, avro_schema, records)
                records = []
    if records:
        if first:
            with open(outfilename, 'wb') as f0:
                fastavro.writer(f0, avro_schema, records)
            f = open(outfilename, 'ab+')
            first = False
        else:
            fastavro.writer(f, avro_schema, records)
    if f:
        f.close()

