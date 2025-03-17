
def solution(n, m, figures):
    # Define the patterns
    patterns = {
        'A': [[1]],
        'B': [[1,1,1]],
        'C': [[1,1],[1,1]],
        'D': [[1,0],[1,1],[1,0]],
        'E': [[0,1,0],[1,1,1]],
    }
    
    # Initialize grid with zeros
    grid = [[0] * m for _ in range(n)]  # this is the way a matrix or a grid is created
    
    # Function to check if pattern can be placed at position (row, col)
    def can_place(pattern, row, col):
        pattern_h, pattern_w = len(pattern), len(pattern[0])
        # Check if pattern fits within grid boundaries
        if row + pattern_h > n or col + pattern_w > m:
            return False
        # Check for overlap
        for i in range(pattern_h):
            for j in range(pattern_w):
                if pattern[i][j] == 1 and grid[row + i][col + j] != 0:
                    return False
        return True
    
    # Function to place pattern at position (row, col)
    def place_pattern(pattern, row, col, figure_idx):
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                if pattern[i][j] == 1:
                    grid[row + i][col + j] = figure_idx + 1
    
    # Process each figure
    for idx, figure in enumerate(figures): # this is the way you take indexes along with items
        pattern = patterns[figure]
        placed = False
        
        # Try each position starting from top-left
        for i in range(n):
            for j in range(m):
                if can_place(pattern, i, j):
                    place_pattern(pattern, i, j, idx)
                    placed = True
                    break
            if placed:
                break
    
    return grid

# Test the example
n, m = 4, 4
figures = ['D', 'B', 'A', 'C']
result = solution(n, m, figures)
for row in result:
    print(row)

"""
PROBLEM STATEMENT:
\"""
you are given a matrix of n,m. also you have been given figures A, B, C, D and E in the form if matrixes as below.

patterns = {
    'A':[[1]],
    'B':[[1,1,1]],
    'C':[[1,1],[1,1]],
    'D':[[1,0],[1,1],[1,0]],
    'E':[[0, 1, 0],[1, 1, 1]],
}


Start with a matrix of all 0s, and use the 1-based index of each figure to represent it on the grid. For example, if figures[0] = 'E' then the shape added to the grid will look like this:

    [[0, 1, 0],
     [1, 1, 1]]

1. Place the figures on the grid in the order they appear in figures. The figures must not overlap any other figures that have already been placed, and they may not be rotated.
2. Of all the available locations, choose the one with the lowest row index.
3. If there are multiple possible locations with the lowest row index, choose the one among them with the lowest column index.
4. It's guaranteed that all figures will fit on the grid.

Return a matrix of integers representing the grid paper after all the figures have been drawn.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(n · m · figures.length) will fit within the execution time limit.

For example:
if  n = 4, m = 4, figures = ['D','B','A','C']
then the method `solution` should return the below
solution(n,m,figures) = [[1,2,2,2],
                         [1,1,3,0],   
                         [1,4,4,0],   
                         [0,4,4,0],   
                        ]
\"""

Instructions:
You have understnad what is being asked?
prepare a simple solution
also add the concetps used to solve the problem from data Structure and algos.
"""