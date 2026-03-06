# PA2-Greedy-Algorithms
COP4533 Programing Assignment Two

# Team
Jennifer Zheng: 52838059  
Srinitha Srikanth: 55178917

# Complie/Build
N/A

# How to Run
To run the program from the root directory: `python src/main.py <input_file>`  
ex: `python src/main.py data/example.in`  
  
  The output should be like this:  
  FIFO  : misses  
  LRU   : misses  
  OPTFF : misses

# Assumptions 
- Input files are stored in the `data` folder 
- Input files should be formatted like this:
    - first line: `k m`
    - second line: `r1 r2 r3 ... rm`
- The number of requests m matches the number of integers provided.
- Request IDs are integers.
- Cache capacity k ≥ 1.
- The program assumes the input file contains all requests on a single line after the first line.

# Question 1: Empirical Comparison
| Input File | k | m | FIFO | LRU | OPTFF |
| ---------- | -- | ---| --- | ---| ------ |
| File1 | 3 | 50 | 45 | 46 | 31 |
| File2 | 6 | 60 | 36 | 30 | 24 |
| File3 | 4 | 60 | 40 | 30 | 26 |  
  
  OPTFF does seem to consistently have the fewest misses.  
  When comparing FIFO to LRU, both have very similar miss counts, but it does seem that LRU is slightly better with misses.
# Question 2: Bad Sequence for LRU or FIFO
For `k=3` there does exists a request sequence for which OPTFF incurs **strictly fewer misses** than LRU/FIFO.  
  
  You can see such behavior when running `file1.in` from the `data` folder and when viewing the table in **Question 1**.  
  | Input File | k | m | FIFO | LRU | OPTFF |
| ---------- | -- | ---| --- | ---| ------ |
| File1 | 3 | 50 | 45 | 46 | 31 |  
  
  In the table you can see that FIFO has 45 misses, LRU has 46 misses, and OPTFF has 31 misses.  
  
  The reason why OPTFF incurs strictly fewer misses than FIFO or LRU in this sequence is due to how OPTFF has future knowledge of what item is not going to be needed for the longest time. LRU and FIFO do not have this future knowledge which can lead them to evict the an item that is needed later on.

# Question 3: Prove OPTFF is Optimal
n/a
