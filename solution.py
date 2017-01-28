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
    
    return [s+t for s in a for t in b]


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
    pass

def only_choice(values):
    pass

def reduce_puzzle(values):
    pass

def solve(grid):
    pass

def search(values):
    pass

diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
display(solve(grid_values(diag_sudoku_grid)))

try:
    from visualize import visualize_assignments
    visualize_assignments(assignments)
except:
    print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
