import sys
import random
from Bio import SeqIO

"""
usage: python select_needed.py INPUT.fasta
"""

def read_input(file):
    """
    Function reads a fasta formatted file of protein sequences
    """
    # print("READING FASTA FILES")
    records = []
    for record in SeqIO.parse(file, "fasta"):
        records.append(record)
    return(records)


if __name__ == "__main__":
    target = {}
    with open("experiment_ids.txt", "r") as f:
        for i, line in enumerate(f):
            target[line[:-1]] = i
    records = read_input(sys.argv[1])
    for record in records:
        if record.id in target:
						
            output_file = "./input_data/batch_" + str(target[record.id] // 1000) + "/input_" + "{:04d}".format(target[record.id]) + ".fa"
            with open(output_file, "w") as fh_out:
                fh_out.write(f">{record.description}\n")
                fh_out.write(f"{record.seq}\n")
