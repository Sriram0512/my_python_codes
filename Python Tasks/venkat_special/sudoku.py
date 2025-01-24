#this function used to print the grid
def matrix(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()

#this function is used to find 0's in the code
def finding_spots(arr, l):
    for row in range(9):
        for col in range(9):
            if (arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False

#it checks wheather the number is already present in the row or not 
def used_in_row(arr, row, num):
    for i in range(9):
        if (arr[row][i] == num):
            return True
    return False

#it checks wheather the number is already present in the coloumn or not
def used_in_col(arr, col, num):
    for i in range(9):
        if (arr[i][col] == num):
            return True
    return False

#it checks wheather the number is already present in the 3x3 box or not
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if (arr[row // 3 * 3 + i][col // 3 * 3 + j] == num):
                return True
    return False

#this function checks is it safe to place the number or not
def check_location(arr, row, col, num):
    return (not used_in_row(arr, row, num) and
            not used_in_col(arr, col, num) and
            not used_in_box(arr, row, col, num))

def solving_sudoku(arr):
    #Main function to solve the Sudoku using backtracking
    l = [0, 0]
    if not finding_spots(arr, l):
        return True
    
    row = l[0]
    col = l[1]

    #trying to fix numbers in empty spots
    for num in range(1, 10):
        if check_location(arr, row, col, num):
            arr[row][col] = num
            
            #Recursively try to solve the rest of the puzzle
            if solving_sudoku(arr):
                return True
            arr[row][col] = 0
    return False

if __name__ == "__main__":
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    if solving_sudoku(grid):
        matrix(grid)
    else:
        print("No solution exists")
