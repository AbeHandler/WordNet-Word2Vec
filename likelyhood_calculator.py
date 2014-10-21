import argparse

parser = argparse.ArgumentParser(description='Generate likelyhood counts')

parser.add_argument('--k_file')

parser.add_argument('--relation_file')

args = parser.parse_args()

relation = {}

with (open(args.relation_file, "r")) as outfile:
	for l in outfile:
		index, value = l.strip("\n").split(",")
		relation[float(index)] = float(value)

total = {}

with (open(args.k_file, "r")) as outfile:
	for l in outfile:
		index, value = l.strip("\n").split(",")
		total[float(index)] = float(value)


for i in range(1, 200):
	print relation[i] / total[i]