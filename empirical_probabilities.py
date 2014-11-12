
syns = []
meros = []
hypers = []
hypos = []
stems = []
holos = []
increments = []

print " & ".join(["Increment", "Synonyms", "Meronyms", "Holonyms", "Hypernyms", "Hyponyms", "Same stem", "None",  "\\\\  \\hline"]).replace("& \\\\", "\\\\")

modder = 0

with open("textfiles/increments.txt") as results:
    counter = 0
    syn_total = 0
    mero_total = 0
    holo_total = 0
    hyper_total = 0
    hypo_total = 0
    stem_total = 0
    none_total = 0
    total_total = 0
    bottom_total = 0
    for line in results.readlines():
        counter += 1
        try:
            line = line.replace("\n", "")
            top, bottom, syn, mero, holo, hyper, hypo, stem, none = [float(n) for n in line.split(",")]
            total = syn + mero + holo + hyper + hypo + stem + none
            if counter == 1:
                bottom_total = bottom
            if counter < 20:
                total_total += total
                mero_total += mero
                syn_total += syn
                holo_total += holo
                hypo_total += hypo
                stem_total += stem
                none_total += none
            else:
                incrementer = round((top + bottom_total)/2, 3)
                if total_total > 0:
                    print " & ".join([str(incrementer),
                                    str(round((syn_total / total_total), 3)),
                                    str(round((mero_total/total_total), 3)),
                                    str(round((holo_total/total_total), 3)),
                                    str(round((hypo_total/total_total), 3)),
                                    str(round((hyper_total/total_total), 3)),
                                    str(round((stem_total/total_total), 3)),
                                    str(round((none_total/total_total), 3)),
                                    "\\\\  \\hline"]).replace("& \\\\", "\\\\")
                else:
                    print " & ".join([str(incrementer),
                                    str(round((syn_total), 3)),
                                    str(round((mero_total), 3)),
                                    str(round((holo_total), 3)),
                                    str(round((hyper_total), 3)),
                                    str(round((hypo_total), 3)),
                                    str(round((stem_total), 3)),
                                    str(round((none_total), 3)),
                                    "\\\\  \\hline"]).replace("& \\\\", "\\\\")
                counter = 0
                syn_total = 0
                mero_total = 0
                holo_total = 0 
                hyper_total = 0
                hypo_total = 0
                stem_total = 0
                none_total = 0
                total_total = 0
                increments_total = 0
        except ValueError:
            pass