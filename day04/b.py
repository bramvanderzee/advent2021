import sys

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

lines = []
with open(fn) as f:
    for l in f:
        lines.append(l.strip())

def check_has_won(board, nums):
    for line in board:
        if len([n for n in line if n in nums]) == 5:
            return True
    pivot = [[row[i] for row in board] for i in range(len(board[0]))]
    for line in pivot:
        if len([n for n in line if n in nums]) == 5:
            return True

    return False

def calc_score(board, nums, final_num):
    unpicked = []

    for line in board:
        unpicked.extend([n for n in line if n not in nums])

    return final_num * sum(unpicked)

picks = [int(n) for n in lines.pop(0).split(',')]
lines.pop(0)

boards = []
for i in range(0, len(lines), 6):
    board = []
    for ix in range(5):
        line = lines[ix + i]
        board.append([int(n) for n in line.split(' ') if not n == ''])
    boards.append(board)

done_picks = [] 
for n in picks:
    to_remove = []
    done_picks.append(n)
    for b in boards:
        if check_has_won(b, done_picks):
            to_remove.append(b)
        if len(boards) == 1:
            print(calc_score(b, done_picks, n))
    for b in to_remove:
        boards.remove(b)