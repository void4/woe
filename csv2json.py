from collections import defaultdict
import csv
import json

reader = csv.reader(open("tree.csv"), delimiter=",", quotechar='"')

a = None

j = defaultdict(lambda:defaultdict(list))


for row in reader:
	if row[0]:
		a = row[0]
	elif row[1]:
		b = row[1]
	elif row[2]:
		c = row[2]
		j[a][b].append(c)

with open("tree.json", "w+") as tree:
	tree.write(json.dumps(j, indent=4))
