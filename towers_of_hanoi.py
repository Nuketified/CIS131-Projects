"""script: towers_of_hanoi.py
   action: a. receive a values for n, starting peg, ending peg, storage peg
           b. test for base case
           c. return a recursive call to towers_of_hanoi()
   author: Mat Bakarich
   date:   04/07/2025 
"""

def towers_of_hanoi(n, start, end, storage):
    """
    Recursive Towers of Hanoi function.
    
    arguments:
        n: the number of disks to move.
        start: starting position of disks.
        end: ending position of disks.
        storage: temporary storage area.
    """
    
    # Base case: move one disk
    if n == 1:
        print(f"{start} -> {end}")  
    
    else:
        # Move n-1 disks from start to storage
        towers_of_hanoi(n - 1, start, storage, end)
        # Move the largest disk from start to end
        print(f"{start} -> {end}")
        # Move n-1 disks from storage to end
        towers_of_hanoi(n - 1, storage, end, start)





# call function for 3 discs moved from peg 1 to peg 3 using peg 2 for storage
towers_of_hanoi(3, 1, 3, 2)