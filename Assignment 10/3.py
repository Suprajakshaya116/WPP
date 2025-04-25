# 3. A magic square is an N×N grid of numbers in which the entries in each row, column and
# main diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for
# N=4, 5, 6, 7, 8
n = 7

# Create a 2D list to store the magic square
magicSquare = [[-1 for _ in range(n)] for _ in range(n)]

# Initialize indices for the first element
x, y = n // 2, n - 1

# Loop to fill the magic square
for i in range(1, n * n + 1):
    # Place the current element at (x, y)
    magicSquare[x][y] = i

    if i % n == 0:
        # If the element is a multiple of n, move left
        y -= 1
    else:
        # Otherwise, move top-right
        x -= 1
        y += 1

    # Apply modulo to avoid going out of bounds
    x = (x + n) % n
    y = (y + n) % n

print(f"Magic Square of n={n}")
for i in range(n):
    for j in range(n):
        print (magicSquare[i][j],end=" ")
    print()
    
