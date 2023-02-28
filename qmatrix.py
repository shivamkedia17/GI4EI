from io import TextIOWrapper
from pathlib import Path
import sys
from typing import List

# Read file
# ensure it's a fastq file
# read a block from the file
# extract line with quality scores
# convert scores to integer list
# append list to a global matrix

def main(): 
    # sys.argv[0] = "qmatrix.py"
    # sys.argv[1] = "ext.fastq"
    
    score_matrix = []

    # get file path
    if (len(sys.argv) != 2):
        print("Usage: python3 qmatrix.py {file_path}.fastq", file=sys.stderr)
        exit(1)
        
    file_path = sys.argv[1]

    # file_path = "ext.fastq"
    
    # check if it's a file of the correct type
    Path(file_path).is_file() and Path(file_path).suffix == '.fastq'

    with open(file_path) as file:
        # iterate over the whole file and generate matrix
        while (True):
            try:
                fastq_seq = read_block(file=file)
                if (check_block(fastq_seq=fastq_seq) == True):
                    score_matrix.append(get_score(scoreLine=get_scoreLine(fastq_seq=fastq_seq)))
                    count+=1
            # if we've reached EOF that is
            except StopIteration as e:
                # print(e)
                break
    print(score_matrix)

# TODO:
# Specify return types
# Type cast inputs

# return a block from the file
def read_block(file: TextIOWrapper):
    block = [next(file).rstrip('\n') for x in range(4)]
    # print(block) 
    return (block)

def check_block(fastq_seq) -> bool:
    if (len(fastq_seq) < 4):
        print("Invalid Read", file=sys.stderr)
        return False

    if (fastq_seq[0][0] != '@'): 
        print("Invalid Fastq File", file=sys.stderr)
        return False

    # add case to check for Non ATCG letters in read seq

    if (fastq_seq[2][0] != '+'): 
        print("Invalid Fastq File", file=sys.stderr)
        return False

    return True

# return the line with the score from a fastq block
def get_scoreLine(fastq_seq):
    # get 4th line from block
    return (fastq_seq[3])

def get_score(scoreLine: str):
    return (list(map(lambda x: ord(x), scoreLine)))

main()
