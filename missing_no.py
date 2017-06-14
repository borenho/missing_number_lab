def find_missing(list1, list2):
    """ 
        Returns the missing number for lists with similar entries and a missing number
    """
    
    # Return 0 for empty lists
    if len(list1) == len(list2) == []:
        return 0

    # Return 0 for lists with the same entries
    if len(list1) == len(list2):
        return 0
        
    if len(list1) > len(list2):
        for x in list1:
            if x not in list2:
                return x
    else:
        for x in list2:
            if x not in list1:
                return x

    """
        A shorthand method could be 'return list(set(list1).symmetric_difference(set(list2)))'
    """

