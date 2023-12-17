from os import listdir
from os.path import isfile, join
import math

# list all files under ./output
files = [f for f in listdir("output") if isfile(join("output", f))]
files.sort()

# counter for mean values
denominator = 0
total_std = 0
total_gmean = 0

# integrate content in all files under ./output
with open('integration.txt', 'w') as outputFile:
  outputFile.write("query_id,best_hit,best_evalue,best_score,score_mean,score_std,score_gmean\n")

  with open('hits_output.csv', 'w') as hitsOutputFile:
    hitsOutputFile.write("fasta_id,best_hit_id\n")

    # read content in all files under ./output
    for file in files:
      filepath = 'output/' + file
      with open(filepath, 'r') as f:
        # skip the column names
        f.readline()
        lines = f.readline()
        outputFile.write(lines)
        items = lines.split(',')

        # record for hits_output and profile_output
        fasta_id = items[0]
        best_hit_id = items[1]
        if (items[5] != 'nan' and items[6] != 'nan'):
          total_std += float(items[5])
          total_gmean += float(items[6])
          denominator += 1
        hitsOutputFile.write(f"{fasta_id},{best_hit_id}\n")

  # print the mean std and mean gmean
  with open('profile_output.csv', 'w') as profileOutputFile:
    profileOutputFile.write("ave_std,ave_gmean\n")
    ave_std = round(total_std/denominator, 2)
    ave_gmean = round(total_gmean/denominator, 2)
    profileOutputFile.write(f"{ave_std},{ave_gmean}\n")