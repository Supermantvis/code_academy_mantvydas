def print_chessboard():
    # loop through rows and columns to print the chessboard
    for row in range(8):
        for col in range(8):
            # use conditional statements to determine whether to print a black or white square
            if (row + col) % 2 == 0:
                print("██", end="")
            else:
                print("  ", end="")
        # move to the next row
        print("\n")

# call the function to print the chessboard
print_chessboard()