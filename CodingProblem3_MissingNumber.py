'''Given an array of integers, find the first missing positive integer
in linear time and constant space. In other words, find the lowest
positive integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.'''

def findMissingNumber(sortList):
    for i in range(len(sortList) - 1):
        if sortList[i] + 1 != sortList[i + 1] and sortList[i] + 1 > 0:
            return sortList[i] + 1
        
    return sortList[len(sortList) - 1] + 1

def main():
    listToSearch = []
    noElements = int(input("How many elements does your list have: "))

    for i in range(noElements):
        element = int(input())

        listToSearch.append(element)

    listToSearch.sort()

    print(findMissingNumber(listToSearch))
    
