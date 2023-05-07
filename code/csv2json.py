import json
fo = open("../data/1.csv", "r")
ls = []
for line in fo:
    line = line.replace("\n", "")
    ls.append(line.split(","))
fo.close()
fw = open("../data/1.json", "w")
for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))
json.dump(ls[1:], fw, sort_keys=True, indent=4)
fw.close()
