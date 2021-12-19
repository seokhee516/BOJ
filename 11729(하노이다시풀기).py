N = int(input())
def move_disk(start_peg, end_peg):
    print(start_peg, end_peg)

def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0:
        return
    
    else:
        other_peg = 6 - start_peg - end_peg
        hanoi(num_disks - 1, start_peg, other_peg)
        
        move_disk(start_peg, end_peg)
        
        hanoi(num_disks - 1, other_peg, end_peg)
print((2**N)-1)
hanoi(N, 1, 3)