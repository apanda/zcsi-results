"""
Compute statistics from result files
"""
import sys
from collections import defaultdict
import argparse
import numpy as np
def stats_header():
	return ("Min", "P5", "Median", "P90", "P95", "P99", "Max")
def compute_stats(values):
	min_val = min(values)
	p5 = np.percentile(values, 5)
	median = np.median(values)
	p90 = np.percentile(values, 90)
	p95 = np.percentile(values, 95)
	p99 = np.percentile(values, 99)
	max_val = max(values)
	return (min_val, p5, median, p90, p95, p99, max_val)

parser = argparse.ArgumentParser(description="Compute statistics from result file", add_help=True)
parser.add_argument('files', nargs='+', metavar='file')
args = parser.parse_args()
rx_data = defaultdict(list)
tx_data = defaultdict(list)
for fname in args.files:
	with open(fname) as f:
		for l in f:
			parts = l.strip().split()
			key = int(parts[0]) # Could be size, delay, or chain length.
			rx = float(parts[1])
			tx = float(parts[2])
			rx_data[key].append(rx)
			tx_data[key].append(tx)
print "Key %s %s"%(' '.join(map(lambda s: "%s_rx"%s, stats_header())), \
					' '.join(map(lambda s:"%s_tx"%s, stats_header())))
for key in sorted(rx_data.iterkeys()):
	values_rx = rx_data[key]
	values_tx = tx_data[key]
	print "%d %s %s"%(key, \
					  ' '.join(map(str, compute_stats(values_rx))), \
					  ' '.join(map(str, compute_stats(values_tx))))
