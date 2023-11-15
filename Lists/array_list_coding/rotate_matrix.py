"""
[
    [1,2,3]    == [00,01,02]
    [4,5,6]    == [10,11,12]
    [7,8,9]    == [20,21,22]
]

===>

[
    [7,4,1]   == [20,10,00]  = [row,column] => [len(matrix)-1-column , row]
    [8,5,2]   == [21,11,01]
    [9,6,3]   == [22,12,02]
]

"""
from __future__ import annotations


def rotate_matrix_90degrees(list_2d: list[list], count=1):
    rotaed_matrix = []
    for iter_count in range(count):
        print(
            f'rotating original matrix by 90 degrees for : {iter_count} time')
        for row in range(len(list_2d)):
            temp_row = []
            for column in range(len(list_2d[0])):
                temp_row.append(list_2d[len(list_2d)-1-column][row])
            print(temp_row)
            rotaed_matrix.append(temp_row)
    print(rotaed_matrix)
    return rotaed_matrix


def rotate(matrix):
    result = []
    for row in range(len(matrix)):
        temp = []
        for col in range(len(matrix[0])):
            temp.append(matrix[len(matrix)-1-col][row])
        result.append(temp)
    print(result)
    return result


rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
