n = len(A)
m = len(B)
C = [[0]* (m+1)] * (n+1)

def LCS (A, B, i, j):
    if (i < 0):
        return 0 
    if (j < 0): 
        return 0
    
    if (A[i] == B[j]):
        C[i][j] = LCS(A, B, i-1, j-1) + 1 
        return C[i][j]
    else: 
        return max(LCS(A, B, i-1, j), LCS(A, B, i, j-1))