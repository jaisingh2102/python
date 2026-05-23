# The code below generates a pattern of odd numbers in a pyramid shape. The variable 'n' determines the number of rows in the pattern. The outer loop iterates through each row, while the inner loop prints the odd numbers for that row. The expression '2 * j - 1' calculates the odd number based on the current value of 'j'.
n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")
    print()