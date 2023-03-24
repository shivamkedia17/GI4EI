# define a function to input a position n in the array,
    # traverse through all the lists and check for the reads at that index
    # count all the possible values
    # make:
        # box plots
        # density distribution
        # histogram   

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from io import TextIOWrapper
from pathlib import Path
import sys


# Read file
# ensure it's a fastq file
# read a block from the file
# extract line with reads
# convert scores to integer list
# append list to a global matrix

def main(): 
    # sys.argv[0] = "qmatrix.py"
    # sys.argv[1] = "ext.fastq"
    
    read_matrix = []

    # get file path
    if (len(sys.argv) != 2):
        print("Usage: python3 qmatrix.py {file_path}.fastq", file=sys.stderr)
        exit(1)
        
    file_path = sys.argv[1]

    # file_path = "ext.fastq"
    
    # check if it's a file of the correct type
    Path(file_path).is_file() and Path(file_path).suffix == '.fastq'

    position = int(input("Enter the position to generate plots: "))

    with open(file_path) as file:
        # iterate over the whole file and generate matrix
        while (True):
            try:
                fastq_seq = read_block(file=file)
                read_length = len(fastq_seq[1])
                if (check_block(fastq_seq=fastq_seq) == True):
                   read_matrix.append(get_read(Line=get_readsLine(fastq_seq=fastq_seq), position=position, length=read_length))

            # if we've reached EOF that is
            except StopIteration as e:
                # print(e)
                break
    # print(read_matrix)
    plot_bar(read_matrix=read_matrix)
    # plot_density(read_matrix=read_matrix)

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
def get_readsLine(fastq_seq):
    # get 2nd line from block
    return (fastq_seq[1])

def get_read(Line: str, position: int, length: int):
    if position < 0 or position >= length:
        print("Index out of Read's range.", file=sys.stderr)
        return False
    
    return Line[position]

def plot_bar(read_matrix):
    bins, counts = np.unique(read_matrix, return_counts=True)
    plt.bar(x=bins, height=counts) 
    plt.xlabel("Base Call")
    plt.ylabel("No. of bases")
    plt.show()

# def plot_density(read_matrix):
    # sns.kdeplot(read_matrix)


main()
