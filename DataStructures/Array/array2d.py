import numpy as np


def insert_into_2d_array(array_to_insert: np.ndarray, index: int, axis: int, data_to_insert: np.array) -> np.array:
    """_summary_

    Args:
        array_to_insert (np.ndarray): _description_
        index (int): _description_
        axis (int): _description_
        data_to_insert (np.array): _description_

    Returns:
        np.array: _description_
    
    Time complexity : O(m)  -> element count to insert
    Space complexity : O(m)  -> element count to insert
    """
    modified_array = np.insert(array_to_insert, index, data_to_insert, axis=axis)
    return modified_array

def access_2d_array_using_index(array_to_access: np.ndarray, 
                                row_index_to_access: int, column_index_to_access: int) -> None:
    """_summary_

    Args:
        array_to_access (np.ndarray): _description_
        row_index (int): _description_
        column_index (int): _description_
    
    Time complexity : O(1)
    Space complexity : O(1)
    """
    try:
        print(f"array_to_access[{row_index_to_access}][{column_index_to_access}] = {array_to_access[row_index_to_access][column_index_to_access]}")
    except Exception as e:
        print(f'Something went wrong exception is {e}')
    finally:
        print('The try except is finished')

def traverse_2d_array(array_to_traverse: np.ndarray) -> None:
    """_summary_

    Args:
        array_to_traverse (np.ndarray): _description_
    Time complexity : O(mn)
    Space complexity : O(1)
    """
    print("Traversing 2d array : Started")
    for row_index, row_val in enumerate(array_to_traverse):
            print(f"Contents of the row {row_val}")
            for column_index, column_val in enumerate(array_to_traverse[row_index]):
                print(f"array_to_access[{row_index}][{column_index}] = {column_val}")
                print(f"Accessing using index is {array_to_traverse[row_index][column_index]}")
    print("Traversing 2d array : Done")
    
    
def search_2d_array(array_to_search: np.ndarray, element_to_search: int) -> None:
    """_summary_

    Args:
        array_to_traverse (np.ndarray): _description_
    Time complexity : O(mn)
    Space complexity : O(1)
    """
    print("Searching 2d array : Started")
    found_flag: bool = False
    for row_index, row_val in enumerate(array_to_search):
            print(f"Contents of the row {row_val}")
            for column_index, column_val in enumerate(array_to_search[row_index]):
                if array_to_search[row_index][column_index] == element_to_search:
                    print(f"Found the element {element_to_search}")
                    found_flag = True
                    break
    if not found_flag:
        print(f"{element_to_search} not found in the given array")
    print("Searching 2d array : Done")


def deleting_2d_array(array_to_delete: np.ndarray, axis: int, index_to_delete: int) -> np.ndarray:
    new_array = np.delete(array_to_delete, index_to_delete, axis=axis)
    return new_array


def main():
    array_2d = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
    print(f"Created 2d Array : {array_2d}")
    array_2d = insert_into_2d_array(array_to_insert=array_2d,index=1,axis=1,data_to_insert=np.array([26,27,28,29,30]))
    print(f"2d Array after inserting column : {array_2d}")
    
    array_2d = insert_into_2d_array(array_to_insert=array_2d,index=-1,axis=0,data_to_insert=np.array([31,32,33,34,35,36]))
    print(f"2d Array after inserting row : {array_2d}")
    access_2d_array_using_index(array_to_access=array_2d, row_index_to_access=5,column_index_to_access=5)
    traverse_2d_array(array_to_traverse=array_2d)
    search_2d_array(array_to_search=array_2d,element_to_search=13)
    
    print(f"Array before deletion is : {array_2d}")
    modified_array = deleting_2d_array(array_to_delete=array_2d,index_to_delete=0,axis=0)
    print(f"Array after deletion is : {modified_array}")
    
    print(f"Array before deletion is : {modified_array}")
    modified_array = deleting_2d_array(array_to_delete=array_2d,index_to_delete=0,axis=1)
    print(f"Array after deletion is : {modified_array}")
    
if __name__ == "__main__":
    main()