'''Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the
original array except the one at i.'''

def productOfArray(array):
    newArray = []
    productEle = 1
    n = 0
    while n < len(array):
        k = array[n]
        for i in range(len(array)):
            if array[i] != k:
                productEle = productEle * array[i]
        newArray.append(productEle)
        productEle = 1
        n += 1
    return newArray

def main():
    newList = []
    noElem = int(input("How many elements does your array have: "))
    for i in range(noElem):
        elem = int(input())

        newList.append(elem)

    print(productOfArray(newList))
