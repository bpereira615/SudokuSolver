assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def cross(A, B):
    """Cross product of elements in A and elements in B.
        
    Args:
        A, B: two strings
    Returns:
        the list formed by all the possible concatenations of a 
        letter s in string A with a letter t in string B
    """
    
    return [s+t for s in A for t in B]




def grid_values(grid):
    """Convert grid into a dict of {square: char} with '.' for empties.
    
    
    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """

    dict = {}
    
    index = 0
    for j in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
        for i in range(1, 10):
        
            curr = j+str(i)

            if grid[index] == '.':
                dict[curr] = '123456789'
            else:
                dict[curr] = grid[index]
            
            index += 1
            
    return dict


def display(values):
    "Display these values as a 2-D grid."
    
    """
    Display the values as a 2-D grid.
    Args: 
        values: the sudoku in dictionary form

    """


    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return



def only_choice(values):
    pass




def reduce_puzzle(values):
    
    """
    Reduce the sudoku puzzle by removing the given number from peers.
    Args: 
        values: the current sudoku in dictionary form
    Return:
        reduced_values: the reduced sudoku in dictionary form
    """
    list = []    
    for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
        for j in range(1, 10):
            
            
            idx = i + str(j)
            if len(values[idx]) == 1:
               list.append(idx)
                      
                
    for curr in list:
        
        num = values[curr]
        for p in peers[curr]:
            values[p] = values[p].replace(num, "")
               
               
    return reduced_values


def solve(grid):
    return grid

def search(values):
    pass






# useful representation of grid into units

rows = 'ABCDEFGHI'
cols = '123456789'

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)









diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
display(solve(grid_values(diag_sudoku_grid)))

try:
    from visualize import visualize_assignments
    visualize_assignments(assignments)
except:
    print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
