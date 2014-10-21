import argparse

parser = argparse.ArgumentParser(description='Generate likelyhood counts')

parser.add_argument('--k_file')

parser.add_argument('--relation_file')

args = parser.parse_args()

print args.k_file

with (open(args.relation_file, "r")) as outfile:
	for l in outfile:
		print l.strip("\n")