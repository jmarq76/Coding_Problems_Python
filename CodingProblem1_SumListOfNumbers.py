'''Given a list of numbers and a number k, return whether any two
numbers from the list add up to k.'''

def SumNumbers(List, k):
    i = 0
    while i < len(List) - 1:
        x = List[i]
        for j in range(len(List) - 1):
            sumOfValue = x + List[j + 1]
            if sumOfValue == k:
                return x, List[j + 1]
        List.remove(x)
    return None

def main():
    List = []
    k = int(input("Which number do you want to be found? "))
    n = int(input("What is the size of your list? "))

    for i in range(0, n):
        element = int(input())

        List.append(element)

    if SumNumbers(List, k) is None:
        print("The sum wasn't found in the array")
    else:
        print(SumNumbers(List, k))
        
    
    
