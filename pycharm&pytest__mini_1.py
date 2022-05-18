# Create a class with name StringClass which should take string as an input from constructor.
# It should have method which should return the length of the string and a method to convert string to list of characters.
# This method will take an argument as string to convert.
class StringClass:
    def __init__(self, Str):
        self.Str = Str

    def lis(self):
        return (list(self.Str))

    def length(self):
        return len(self.Str)


# Create class PairsPossible which should inherit from StringClass and should have a method for storing list of all possible pairs formed.
# It should also have a method to print list of every possible pair in same line but with space between them.
# Pairs should be in list.
class PairsPossible(StringClass):
    def pairs(self, list):
        res = [(n, ob1) for idx, n in enumerate(list) for ob1 in list[idx + 1:]]
        print(res)


# Create a class SearchCommonElements which should take up a string.
# Your task is to create a method to find common elements from string taken in StringClass and string taken in PairsPossible class and return the answer in list.
# Note- Please use dictionary logic to find common elements
class SearchCommonElements(StringClass):
    def common(self, st, Str):
        a = list(set(st) & set(Str))
        print(a)


# Create a class EqualSumPairs to get the count of total number of pairs formed in class PairsPossible which has sum which is not equal to sum of other pairs.
# Print the output for SearchCommonElements and EqualSumPairs classes

class EqualSumPairs:
    def pairs2(self, list):
        res = [sum((int(n), int(ob1))) for idx, n in enumerate(list) for ob1 in list[idx + 1:]]
        print(set(res))
        print(len(set(res)))


n = input("Enter a string :")
ob1 = StringClass(n)
print(ob1.lis())
print(ob1.length())
h = ob1.lis()
ob2 = PairsPossible(ob1)
ob2.pairs(h)
st = input("Enter string to compare ")
ob3 = SearchCommonElements(ob1)
ob3.common(n, st)
ob4 = EqualSumPairs()
ob4.pairs2(h)