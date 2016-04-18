"""
Compute statistics from result files
"""
import sys
from collections import defaultdict
import argparse
import csv
parser = argparse.ArgumentParser(description="Combine files into one", add_help=True)
parser.add_argument('-c,--column', required=True, help="Column to retain/combine one", metavar="column", \
		dest="columns", action='append')
parser.add_argument('files', nargs='+', metavar='file,title')
args = parser.parse_args()
all_keys = set()
data = defaultdict(list)
header = []
header.append('Key')
for name_title in args.files:
	(fname, title) = name_title.split(',')
	for column in args.columns:
		header.append('%s:%s'%(title,column))
	with open(fname) as csvfile:
		reader = csv.DictReader(csvfile, delimiter=' ')
		for l in reader:
			key = int(l['Key'])
			for column in args.columns:
				data[key].append(l.get(column, ''))
print ','.join(map(str, header))
for k in sorted(data.iterkeys()):
	print "%s,%s"%(k, ','.join(map(str, data[k])))

