""" 
1D array Practice
"""

from array import *
from array1d import *

def main():
    # 1. Create and traverse an array
    int_array = array.array('i',[1,2,3,4,5])
    traverse_array(array_to_traverse=int_array)
    
    # 2. Access the array elements using index
    access_array_elements(array_to_access=int_array, index_to_access=3)
    
    # 3. Append the elements to the array (Can only be appended at the end of the array)
    int_array.append(6)

    # 4. Insert the elements into the array using insert method
    insert_into_array(array_to_insert=int_array, index_to_insert=2, data_to_insert=22)
    
    # 5. Extend python array using extend method
    int_array_2 = array.array('i',[10,11,12,13,14,15,16,17,18,19,20])
    int_array.extend(int_array_2)
    print(f"After extending python array is {int_array} and size is {len(int_array)}")
    
    # 6. Adding items from list into python array using fromlist method
    temp_list = [100,107,101,102,103,104,105,106,107,107, 108]
    int_array.fromlist(temp_list)
    print(f"After adding fromlist python array is {int_array}")

    # 7. Remove element from array using remove
    delete_element_from_array(element_to_delete=100,array_to_delete=int_array)
    
    # 8. Remove element from array using pop method
    element_removed = int_array.pop()
    print(f"Removed element {element_removed} from array")
    print(f"Array after removing last element is {int_array}")
    
    # 9. Get the index of element in array
    element_index = int_array.index(107)
    print(f"Index of 107 is {element_index}")
    
    # 10. Reversing the array using reverse method
    int_array.reverse()
    print(f"Array after reversing element is {int_array}")
    
    # 11. Get array buffer information through buffer_info method
    print(f"Buffer information is {int_array.buffer_info()}")
    
    # 12. Check the number oc occurrences of a element in the array
    print(f"Occurrence count of 107 is {int_array.count(107)}")
    
    # 13. Convert the array to a string
    string_array = int_array.tobytes()
    print(f"Converted array is {string_array}")
    
    # 14. Convert the array from byte string to array
    ints = array.array("i")
    ints.frombytes(string_array)
    print(f"Converted array is {ints}")

    # 15. Convert the array to list
    int_list = int_array.tolist()
    print(f"Converted array to list is {int_list}")
    
    # 16. Slice elements from array
    print(f"Sliced array is {int_array[1:4]}")
    
    
    




if __name__ == '__main__':
    main()