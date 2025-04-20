# modifications required to print correct answer

ROWS = 3
COLS = 6

matrix = [[0]*COLS]* ROWS

pri = 
fib = 
squ = [1, 4, ?, ?, ?, ?]

# no changes below this line
for i in range(COLS):
    matrix[0][i] += pri[i]
    matrix[1][i] += fib[i]
    matrix[2][i] += squ[i]

m = matrix

print(chr(m[0][0]*m[1][5] + 88), chr(m[1][0]+m[2][5]+ 65), chr(m[0][3]*m[2][2]+41), chr(m[0][2]*m[2][2]+60), chr(m[0][5]*m[1][4]+71), chr(m[2][0]*m[2][4]+75))