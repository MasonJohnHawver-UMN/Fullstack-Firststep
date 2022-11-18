import pickle

data = []
tags = {'QUANTITY', 'TEMP', 'SIZE', 'NAME', 'STATE', 'UNIT', 'DF'}

for fn_read, fn_write in [("data/ar_gk_train.tsv", "data/train.bin"), ("data/ar_gk_test.tsv", "data/test.bin")]:
    with open(fn_read) as fr:
        lines = [ line.strip().split('\t') for line in fr.readlines() ]

        i = 0
        while i < len(lines):

            start = i
            while i < len(lines) and len(lines[i]) == 2: i += 1
            end = i

            text = " ".join([line[0] for line in lines[start : end]])
            text = text.replace("-LRB-", "(")
            text = text.replace("-RRB-", ")")

            ents = []
            for line in lines[start: end]:
                index = text.find(line[0])
                tag = line[1]
                if tag in tags:
                    ents.append((index, index + len(line[0]), tag))

            print(ents)

            if text.strip() != "":
                data.append({"entities" : ents, "text" : text})

            i += 1


    with open(fn_write, "wb") as f:
        pickle.dump(data, f)
