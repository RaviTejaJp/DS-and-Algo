list1 = [1,2,3,4,5,6,7,8,9,10]

# Slicing works bit differently here. What ever you want to replace with will get replaced as a whole
list1[0:1] = [10,20,30]

print(f"List after slicing : {list1}")

#Pop method with no index last element gets popped
list1.pop()
print(f"List after Popping : {list1}")

# Pop method using index
# Time complexity using index 0(n)
# Space complexity using index 0(1)
list1.pop(5)
print(f"List after Popping : {list1}")

#delete method
# Time complexity using index 0(n)
# Space complexity using index 0(1)
del list1[0]
print(f"List after Deleting : {list1}")

del list1[2:4]
print(f"List after Deleting : {list1}")

# remove method
# Time complexity using index 0(n)
# Space complexity using index 0(1)
list1.remove(20)
print(f"List after Removing : {list1}")


# Search for element in the list
target = 9

# Time complexity for search :  0(n) -- uses linear search
# Space complexity for search : 0(1)
if target in list1:
    print(f"Target : {target} found in list")
else:
    print(f"Target : {target} not found in list")


# List Operations

# Concatenate
list2 = [10,20,30,40,50]
list3 = [60,70,80,90,100]

result = list2+list3
print(f"List after concatenating : {result}")
print(f"Using * operator : {[1,2]*4}")

print(f"Length of the list : {len(list1)}")
print(f"Max of the list : {max(list1)}")
print(f"Min of the list : {min(list1)}")
print(f"Sum of the list : {sum(list1)}")
print(f"Average of the list : {sum(list1)/len(list1)}")

a = 'spam'
b = list(a)
print(f"{a} as list is {b}")

a = "This is a very good example"
b = a.split()
print(f"{a} as split list is {b}")

a = "This-is-a-very-good-example"
delimiter = "-"
b = a.split(delimiter)
print(f"{a} as split list is {b}")

delimiter = " "
print(f"joining the list using delimiter : {delimiter.join(b)}")

# List comprehension
list4 = [item*2 for item in list1]
print(f"List 4 created from list1 using comprehension : {list4}")

list5 = [item for item in list4 if item % 10 == 0]
print(f"List 5 created from list4 using conditional comprehension : {list5}")


def is_consonant(letter: str) -> bool:
    if letter.lower() not in "aeiou" and letter.isalpha():
        return True
    return False

sentence = "I am trying to take only consonants from this statement"

consonants = [item for item in sentence if is_consonant(item)]
print(f"consonants from sentence is {consonants}")
consonants = [item*2 if is_consonant(item) else " " for item in sentence]
print(f"consonants from sentence is {consonants}")
consonants = [is_consonant(item) for item in sentence]
print(f"consonants from sentence is {consonants}")