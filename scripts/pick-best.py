"""
When running packet size evaluation, we vary the number of ports used as a way to pick whatever is the best performance
achievable with a given packet size. This script selects the best run from among these runs.
"""
import sys
from collections import defaultdict
import argparse
parser = argparse.ArgumentParser(description="Pick results from a file", add_help=True)
parser.add_argument('files', nargs='+', metavar='file')
parser.add_argument('-d,--decisions', help='Output decisions to this file', dest='decision')
args = parser.parse_args()
decision_file = None
if args.decision:
	decision_file = open(args.decision, "w")
for fname in args.files:
	with open(fname) as f:
		by_size = defaultdict(list)
		for l in f:
			parts = l.strip().split()
			by_size[int(parts[0])].append((int(parts[1]), (float(parts[2]), float(parts[3]))))
		for k in sorted(by_size.iterkeys()):
			v = by_size[k]
			v_sorted = sorted(v, key=lambda (n, v): v, reverse=True)
			pick = v_sorted[0]
			if decision_file:
				print >>decision_file, "For %d picked %d"%(k, pick[0])
			print "%d %f %f"%(k, pick[1][0], pick[1][1])
