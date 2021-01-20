import re
import io

def count_motifs(seq, motif):
    pieces = re.split(motif, seq)
    return len(pieces) - 1

fhandle = io.open("grape_promoters.txt", "rU")

for line in fhandle:
    linestripped = line.strip()
    line_list = re.split(r"\s+", linestripped)
    gid = line_list[0]
    seq = line_list[1]

    num_motifs = count_motifs(seq, r"[AT]GATA[GA]")
    print(gid + "\t" + str(num_motifs))

fhandle.close()