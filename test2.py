#_Здравствуйте, Никита, я застопорился на матрице module_2_5, что не так?
def get_matrix(n, m, value):
    n = 3
    m = 5
    value = 42
    for value in range(n):
        for _ in range(m):
            result = get_matrix(n, m, value)
            print(result)

            #_хотя, я могу написать так:
n = 3
m = 5
value = 42
matrix = [[value for _ in range(m)] for _ in range(n)]
result2 = matrix
print(result2) #_и всё получится
