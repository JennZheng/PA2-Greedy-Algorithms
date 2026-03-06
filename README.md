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

Let OPTFF be Belady’s Farthest-in-Future algorithm. Let ( A ) be any offline algorithm that knows the full request sequence. Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.

First, we want to look at reduced schedules. We only bring an item into the cache when it is requested and not already in the cache. Any offline algorithm can be converted into such a reduced schedule without increasing its number of misses. Let SF be the schedule produced by OPTFF and let S be any optimal reduced schedule (with the minimum possible number of misses). 

We can prove with induction on the time step j that there exists an optimal reduced schedule that agrees with OPTFF on all evictions up through step j. For the inductive step, before request j + 1, both schedules have exactly the same cache contents. If the next requested item is already in cache, neither schedule evicts anything. If not in cache, and both schedules evict the same item, they continue to agree. 

The only interesting case is when the item is not in the cache and OPTFF evicts some page e while the optimal schedule s evicts a different page 
f. We modify S so that at step j + 1, it evicts e instead of f, and them carefully "follow" the sold S from that point on. We let the modified schedule imitate S until the first time on of those two pages, e or f, is involved. Then we adjust a single evication at that moment so that afterward the two schedules' caches are the same. The local swap never causes more misses than S because OPTFF chose the page whose next use is farthest in the future. Then, we obtain a new optimal reduced schedule that agrees with OPTFF one more step to the right. Induction allows us to tranform some optimal schedule into one that matches OPTFF at every step without increasing misses, which implies that OPTFF itself has no more misses than any offline algorithm and therefore is optimal. 

