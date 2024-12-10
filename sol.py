import copy
import time
import visualizer


class Board:
    SIZE = 56

    def __init__(self):
        self.grid = [[True for _ in range(Board.SIZE)] for _ in range(Board.SIZE)]  # grid[y][x] = True if unoccupied
        self.next_free = (0, 0)  # (x, y), the top leftmost free cell
        self.space = Board.SIZE * Board.SIZE  # free space on this board

    ''' Returns True if this piece fits at the top leftmost free space '''
    def does_fit(self, piece):
        # Ensure this piece fits within the bounds of the board
        if self.next_free[0] + piece[0] > Board.SIZE or self.next_free[1] + piece[1] > Board.SIZE:
            return False

        # Ensure each cell is free
        for w in range(piece[0]):
            for h in range(piece[1]):
                if not self.grid[self.next_free[1] + h][self.next_free[0] + w]:
                    return False

        return True

    ''' Inserts this piece at the top leftmost free position
        Assumes this piece fits 
        Returns the top left of this inserted piece '''
    def insert(self, piece):
        position = copy.copy(self.next_free)

        # Fill in the cells occupied by this piece
        for x in range(piece[0]):
            for y in range(piece[1]):
                self.grid[self.next_free[1] + y][self.next_free[0] + x] = False

        # Update top-leftmost free position
        updated = False
        for y in range(Board.SIZE):
            for x in range(Board.SIZE):
                if not updated and self.grid[y][x]:
                    self.next_free = (x, y)
                    updated = True

        # Update remaining space
        self.space -= piece[0] * piece[1]

        return position

    ''' Return a copy of this board '''
    def copy(self):
        copied_board = Board()
        copied_board.grid = copy.deepcopy(self.grid)
        copied_board.next_free = copy.copy(self.next_free)
        copied_board.space = self.space
        return copied_board


def get_solution(board, remaining, positions):
    visualizer.visualize(positions)  # Visualize positions at each recursive step

    if board.space == 0:
        return positions

    for piece in remaining:
        for isRotated in (False, True):
            rotated_piece = piece if not isRotated else (piece[1], piece[0])
            if board.does_fit(rotated_piece):
                # Insert piece into board, remove piece from remaining, append position
                new_board = board.copy()
                new_remaining = copy.deepcopy(remaining)
                position = new_board.insert(rotated_piece)
                new_remaining.remove(piece)
                positions.append((rotated_piece, position))  # Add position of piece

                # Get recursive solution
                solution = get_solution(new_board, new_remaining, positions)
                if solution:
                    return solution

                # Revert unsuccessful position addition
                positions.pop()


''' ======================= Run the Code ======================= '''
visualizer = visualizer.Visualizer()

all_pieces = [(28, 14), (21, 18), (21, 18), (21, 14), (21, 14), (32, 11), (32, 10), (28, 7), (28, 6), (17, 14), (14, 4), (10, 7)]
board = Board()

# Call the solution function and print the result
result = get_solution(board, all_pieces, [])
print(result)

time.sleep(25)
