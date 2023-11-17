from __future__ import annotations


def isPermutation(string1: str, string2: str) -> bool:
    """_summary_

    Args:
        string1 (str): _description_
        string2 (str): _description_

    Returns:
        bool: _description_
    """
    if len(string1) != len(string2):
        return False
    else:
        string1 = list(string1)
        string2 = list(string2)
        for item in string1:
            if item in string2:
                string2.remove(item)
            else:
                return False
        if string2 == []:
            return True
    return False


print(isPermutation('RAILL', 'LIARR'))
