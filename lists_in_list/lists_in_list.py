
def numbers_in_list(main_list):
    """The function takes a list. This list contains lists with ranges of numbers. If all numeric ranges overlap, True is returned, if not, False."""

    all_numbers_list = lambda x: list(range(x[0], x[1]+1)) #function convert range to list with numbers
    all_list = list(map(all_numbers_list, main_list)) # convert all ranges in list

    for item in all_list: # take one list with numbers
        for next_item in all_list: # compare it to everyone else
            flag = set(item).isdisjoint(set(next_item)) # if elements set(item) NOT IN set(next_item) return True
        if flag: # item (not &) next_item
            return False
    return True
            
                
main_list = [[2,10],[3,10],[5,20],[2,50],[9,100],[5,15]]

print(numbers_in_list(main_list))

