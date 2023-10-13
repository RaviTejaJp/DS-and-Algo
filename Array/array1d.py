import array

def insert_into_array(array_to_insert: array, data_to_insert: int, index_to_insert: int) -> None:
    """ 
    Insertion into array

    1. Inserting at the beginning of the array - most time consuming action as every element needs to be shifted
    2. Inserting at the end of the array - Fastest as it doesn't need to shift elements
    3. Inserting at the middle of the array - Depends on the element location where we are inserting
    
    Note: If we give a index that is greater than the length of the array it just insert at the end of the array
    """
    print(f"Array before insertion of the element is : {array_to_insert}")
    array_to_insert.insert(index_to_insert,data_to_insert)
    print(f"Array after inserting the element at the start of the index is {array_to_insert}")

    """ 
    Time complexity of insertion at the beginning of the array is O(n)
    Space Complexity of insertion at the beginning of the array is O(1)
    """


def traverse_array(array_to_traverse: array) -> None:
    """ 
    Traversing through the array
    """
    print("Traversing through the array")
    for item in array_to_traverse:
        print(item)
    print("Done Traversing through the array")

    """ 
    Time complexity of traversing through the array is O(n)
    Space Complexity of traversing trough array is O(1)
    """


def access_array_elements(array_to_access: array, index_to_access: int) -> None:
    """_summary_ : Tries to access the elements of the array using index.
    If finds print the index and value of the element
    else prints not found

    Args:
        array_to_access (array): _description_ : Array to access index
        index_to_access (int): _description_ : Index to access in given array

    Returns:
        None
    """
    if index_to_access >= len(array_to_access):
        print("Index out of range")
    elif index_to_access < -1*len(array_to_access):
        print("Negative index out of range")
    else:
        print(f"Element at index {index_to_access} in given array is : {array_to_access[index_to_access]}")
    """
    Time Complexity of accessing the elements in an array by index : O(1)
    Space Complexity of accessing the elements in an array by index : O(1)
    """


def search_for_element_in_array(array_to_search: array, element_to_search: int) -> None:
    """_summary_ : Search for element in array using linear search

    Args:
        array_to_search (array): _description_
        element_to_search (int): _description_

    Returns:
        None
    """
    found_flag = False
    for item in array_to_search:
        if item == element_to_search:
            found_flag = True
            print(f"Found element {element_to_search} in array")
            break
    if not found_flag:
        print(f"Did not find element {element_to_search}")
    """ 
    Time Complexity of Searching elements in an array using linear search is : O(n)
    Space Complexity of Searching elements in an array using linear search is : O(1)    
    """
def delete_element_from_array(array_to_delete: array, element_to_delete: int) -> None:
    """_summary_ : delete the first occurrence of matching element

    Args:
        array_to_delete (array): _description_
        element_to_delete (int): _description_
    """
    try:
        array_to_delete.remove(element_to_delete)
    except Exception as e:
        print(f'Something went wrong : {e}')
    else:
        print(f"Deleted element {element_to_delete} from array")
    finally:
        print('The delete_element_from_array function call is finished')
    """ 
    Time Complexity of Deleting elements in an array is : O(n)
    Space Complexity of Deleting elements in an array is : O(1)
    """
    
    
def main():
    """ 
    Creation of array
        1. Using array - inbuilt library
        2. Using numpy - need to install
    """

    int_array = array.array('i',[1,2,3,4,5])
    print(int_array)
    for item, data in enumerate(int_array):
        print(f"{item} --- address --- {hex(id(data))}")    


    import numpy as np
    int_np_array = np.array([1,2,3,4], dtype=int)
    print(int_np_array)
    for item, data in enumerate(int_np_array):
        print(f"{item} --- address --- {hex(id(data))}")    
    """ 
    Time complexity:
        To create an empty array : O(1)
        To create an n size array : O(n)

    Space complexity:
        To create an empty array : O(1)
        To create an n size array : O(n)
    """
    insert_into_array(array_to_insert=int_array,data_to_insert=10,index_to_insert=0)
    insert_into_array(array_to_insert=int_array,data_to_insert=10,index_to_insert=0)

    traverse_array(array_to_traverse=int_array)

    access_array_elements(array_to_access=int_array, index_to_access=10)
    access_array_elements(array_to_access=int_array, index_to_access=-10)
    access_array_elements(array_to_access=int_array, index_to_access=3)
    access_array_elements(array_to_access=int_array, index_to_access=-2)

    search_for_element_in_array(array_to_search=int_array, element_to_search=12)
    search_for_element_in_array(array_to_search=int_array, element_to_search=1)


    delete_element_from_array(array_to_delete=int_array, element_to_delete=12)
    delete_element_from_array(array_to_delete=int_array, element_to_delete=10)

    traverse_array(array_to_traverse=int_array)

if __name__ == '__main__':
    main()