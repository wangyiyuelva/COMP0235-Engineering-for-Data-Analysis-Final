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
    records = []
    for record in SeqIO.parse(file, "fasta"):
        records.append(record)
    return(records)


if __name__ == "__main__":
    # Filter out 6000 target protein IDs and their corresponding sequences
    # a dictionary for target protein IDs and given number for batches
    target = {}
    with open("experiment_ids.txt", "r") as f:
        for i, line in enumerate(f):
            # skip the '\n'
            target[line[:-1]] = i
    records = read_input(sys.argv[1])
    for record in records:
        if record.id in target:
            #  categorize each task into batches according to its given number
            output_file = "./input_data/batch_" + str(target[record.id] // 1000) + "/input_" + "{:04d}".format(target[record.id]) + ".fa"
            with open(output_file, "w") as fh_out:
                fh_out.write(f">{record.description}\n")
                fh_out.write(f"{record.seq}\n")
