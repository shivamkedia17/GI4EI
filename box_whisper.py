from io import TextIOWrapper
from pathlib import Path
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# take input into a numpy array -> append the new line to a 2D matrix, don't make a list of lists
# transpose numpy array
# run calculations per position wise

score_matrix = []
plot_matrix = []

def main(): 
    
    if check_usage:
        file_path = sys.argv[1]

    global score_matrix

    if not check_input(file_path=file_path):
        sys.exit(2)
    
    gen_scoreMatrix(file_path=file_path)
    score_matrix = np.matrix(score_matrix)
    # print(score_matrix)
    # print(score_matrix.T)

    # score_matrix = score_matrix.T
    # print(len(score_matrix))

    # print(score_matrix[1])

    # for i in range(len(score_matrix)):
        # plot_for_position(i)

    r,c = score_matrix.shape
    fig, ax = plt.subplots()

    meanline_x = np.array(np.arange(1, c+1))
    meanline_y = np.matrix(np.mean(score_matrix, 0)).A1
    # print(meanline_x)
    # print(meanline_y)
    
    # import pdb; pdb.set_trace()
    
    # breakpoint
    
    # plot the boxes in boxplot
    ax.boxplot(x=score_matrix, sym='', widths=0.75, capwidths=0.7,
                patch_artist=True, medianprops={"color": "red"},
                boxprops={"facecolor": "yellow", "edgecolor": "black"},
                )



    # print(c) # No. of columns in the matrix

    ax.set_ylim(0,42)
    # for i in range(0, l, 2):

    ax.axvspan(xmin=1-0.35, xmax=c+0.35, ymin=0, ymax=0.55, facecolor='green', alpha=0.2)
    ax.axvspan(xmin=1-0.35, xmax=c+0.35, ymin=0.55, ymax=0.775, facecolor='yellow', alpha=0.2)
    ax.axvspan(xmin=1-0.35, xmax=c+0.35, ymin=0.775, ymax=1, facecolor='red', alpha=0.2)
      # ax.axvspan(xmin=score_matrix[i+1], xmax=score_matrix[i+2], ymin=0, ymax=20/36, facecolor='green', alpha=0.4)
        # ax.axvspan(xmin=(100*i/l), xmax=100*(i+1)/l, ymin=0, ymax=20/36, facecolor='green', alpha=0.2)
    # plt.axes.Axes.axvspan(xmin=0, xmax= 1, ymin=0, ymax=0.55, alpha=0.5)

    # Plot the blue line denoting per base average
    ax.plot(meanline_x, meanline_y, 'b', linewidth=0.7)

    plt.xticks(ticks=np.arange(1,c+1,2), fontsize=10)
    plt.yticks(ticks=np.arange(0,43,2), fontsize=10)
    plt.xlabel("Position in read (bp)")
    plt.rcParams['font.size'] = '10'
    plt.show()

    
    # sns.catplot(data=score_matrix.T, kind = "box")

    # sns.show()

    
    
def check_usage():
    # get file path
    if (len(sys.argv) != 2):
        print("Usage: python3 qmatrix.py {file_path}.fastq", file=sys.stderr)
        exit(1)
    else:
        return True


def check_input(file_path:str) -> bool:
    # check if it's a file of the correct type
    if not(Path(file_path).is_file() and Path(file_path).suffix == '.fastq'):
        print("The input file is incorrect/doesn't exist.", file=sys.stderr)
        return False
    else:
        return True


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
    return (list(map(lambda x: ord(x)-33, scoreLine)))

def gen_scoreMatrix(file_path: str):
    global score_matrix 

    with open(file_path) as file:
        # iterate over the whole file and generate matrix
        while (True):
            try:
                fastq_seq = read_block(file=file)
                if (check_block(fastq_seq=fastq_seq) == True):
                    score_matrix.append(get_score(scoreLine=get_scoreLine(fastq_seq=fastq_seq)))
            # if we've reached EOF that is
            except StopIteration as e:
                # print(e)
                break

def plot_for_position(pos: int):
    global score_matrix
    global plt
    # print(score_matrix[pos])
    plt.boxplot(x=score_matrix[pos], sym='')



    # x = []
    # for line in score_matrix:
    #     x.append(line[pos])
    
    # x_max = max(x)
    # x_min = min(x)
    # x_median = np.median(x)
    # x_upper_quartile = np.quantile(x, q=0.75)
    # x_lower_quartile = np.quantile(x, q=0.25)

    # x = np.array(x)
    # print("Pos:", pos, "data:", x)
    # sns.catplot(data=x, kind= "box")

main()
