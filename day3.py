## part 1 ##
file = open("input3.txt", "r")

map_grid = []
numbers = '0123456789'
all_numbers = []
dots_and_numbers = ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\n']
valid = False

for line in file:
    map_grid.append(line)


for row_index, row in enumerate(map_grid):
    number = ""
    for col_index, col in enumerate(row):
        if col in numbers:
            number += col
            # validation for if its near a symbol
            # up
            try:
                if map_grid[row_index-1][col_index] not in dots_and_numbers:
                    valid = True
            except:
                print('', end="")
            
            # down
            try:
                if map_grid[row_index+1][col_index] not in dots_and_numbers:
                    valid = True
            except:
                print('', end="")

            # left
            try:
                if map_grid[row_index][col_index-1] not in dots_and_numbers:
                    valid = True
            except:
                print('', end="")

            # right
            try:
                if map_grid[row_index][col_index+1] not in dots_and_numbers:
                    valid = True
            except:
                print('', end="")

            # diagonal
            try:
                if map_grid[row_index+1][col_index+1] not in dots_and_numbers:
                    valid = True
            except:
                print('', end="")
            
            try:
                if map_grid[row_index-1][col_index-1] not in dots_and_numbers:
                    valid = True
            except:
                print('', end="")

            try:
                if map_grid[row_index-1][col_index+1] not in dots_and_numbers:
                    valid = True
            except:
                print('', end="")
            
            try:
                if map_grid[row_index+1][col_index-1] not in dots_and_numbers:
                    valid = True
            except:
                print('', end="")

                
        else:
            if number != "" :  
                if valid:
                    all_numbers.append(int(number))
            number = ""
            valid = False

print(sum(all_numbers))