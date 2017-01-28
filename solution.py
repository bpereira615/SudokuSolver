assignments = []



rows = 'ABCDEFGHI'
cols = '123456789'

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

    values = []
    all_digits = '123456789'
    for c in grid:

        #if value unkonwn, set as all possible digits
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)

    #check that valid input is given (9x9)
    assert len(values) == 81

    #create dictionary from pair box - value pairs
    return dict(zip(boxes, values))



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
    
    """Sets given square to final choice if the only choice for given number among peers
    
    
    Args:
        values: sudoku grid as dictionary
    Returns:
        values: udated sudoku grid
    """

    #check all units (in order: rows, columns, squares)
    for unit in unitlist:

        #check each possible value
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]

            #check for single ocurrence, set if found
            if len(dplaces) == 1:
                values = assign_value(values, dplaces[0], digit)
    return values




def reduce_puzzle(values):
    
    """
    Reduce the sudoku puzzle by removing the given number from peers.
    Args: 
        values: the current sudoku in dictionary form
    Return:
        reduced_values: the reduced sudoku in dictionary form
    """
    list = []    
    for curr in boxes:
        
        if len(values[curr]) == 1:
            list.append(curr)
                      
                
    for curr in list:
        
        num = values[curr]
        for p in peers[curr]:

            reduced_values = assign_value(values, p, values[p].replace(num, ''))
               
               
    return reduced_values


def solve(grid):
    return grid

def search(values):
    pass






# useful representation of grid into units



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
