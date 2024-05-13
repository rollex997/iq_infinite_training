# Remove duplicate lists in tuples(Preserving Order)
# Using OrderedDict() + tuple()
from collections import OrderedDict
 
# Initializing tuple 
test_tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
 
# printing original tuple 
print("The original tuple is : " + str(test_tup))
 
# Remove duplicate lists in tuples(Preserving Order)
# Using OrderedDict() + tuple()
res = list(OrderedDict((tuple(x), x) for x in test_tup).values())
 
# printing result
print("The unique lists tuple is : " + str(res))

class RemoveDuplicateTuples : 
    def __init__(self, var_tuple):
        self.__var_tuple = var_tuple
    def get_tuple(self):
        return self.__var_tuple
    def remove_duplicates(self):
        var_tuple = self.__var_tuple
        res = list(OrderedDict((tuple(x),x) for x in var_tuple).values())
        return res