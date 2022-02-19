
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

#My first solution to "Plus minus"
# def plusMinus(arr):
#     negative = 0
#     positive = 0
#     zero = 0
#     amount = len(arr)
#     for i in range (len(arr)):
#         if arr[i] < 0:
#             negative += 1
#         elif arr[i] > 0:
#             positive +=1
#         else:
#             zero += 1
#     print(positive/amount)
#     print(negative/amount)
#     print(zero/amount)

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))
 
#     plusMinus(arr)

#Diagonal
def diagonalDifference(arr):
    num = len(arr)
    first = 0
    second = 0
    for i in range(0, num):
        first += arr[i][i]
        second += arr[i][num - i - 1]
        
    return abs(first - second)

this_array = [3][3]
print(diagonalDifference(this_array))