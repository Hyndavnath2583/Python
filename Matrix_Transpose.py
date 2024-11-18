'''Interchanging of rows and columns is transpose'''
def get_transpose_of_matrix(matrix, m, n):
    # Complete this function=
    for i in range(0,n):
        k=[]
        for j in range(0,m):
            k.append(matrix[j][i])
        print(k)

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

# Call the get_transpose_of_matrix function
get_transpose_of_matrix(num_list, m, n)
