#These are the problems I have completed thus far. I put in the starter code for the questions for context, but the code inside the functions is my code :)
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
# def diagonalDifference(arr):
#     num = len(arr)
#     first = 0
#     second = 0
#     for i in range(0, num):
#         first += arr[i][i]
#         second += arr[i][num - i - 1]
        
#     return abs(first - second)
# this_array = [
#     #0
#     [7, 4, 5], 
#     #1
#     [-5, 8, 9],
#     #2
#     [5, 7, 8]]
# print(diagonalDifference(this_array))
# print(this_array)
#!/bin/python3
#This came after a long time of thinking and looking at other solutions! A lovely one line answer to this problem!
# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'miniMaxSum' function below.
# #
# # The function accepts INTEGER_ARRAY arr as parameter.
# #

# def miniMaxSum(arr):
#     print(sum(arr)-max(arr), sum(arr)-min(arr))
        

# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'timeConversion' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.
# #

# def timeConversion(s):
#     if s[-2:] == "AM" and s[0:2] == "12":
#         return("00" + s[2:-2])
#     elif s[-2:] == "PM" and s[0:2] == "12" or s[-2:] == "AM":
#         return(str(s[:-2]))
#     elif s[-2:] == "PM":
#         return(str(int(s[:2])+12)+s[2:-2])
        

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

# def matchingStrings(strings, queries):
#     results = []
#     for i in queries:
#         results.append(strings.count(i))
#     return results
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     strings_count = int(input().strip())

#     strings = []

#     for _ in range(strings_count):
#         strings_item = input()
#         strings.append(strings_item)

#     queries_count = int(input().strip())

#     queries = []

#     for _ in range(queries_count):
#         queries_item = input()
#         queries.append(queries_item)

#     res = matchingStrings(strings, queries)

#     fptr.write('\n'.join(map(str, res)))
#     fptr.write('\n')

#     fptr.close()

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'lonelyinteger' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts INTEGER_ARRAY a as parameter.
# #

# def lonelyinteger(a):
#     for i in range(len(a)):
#         count = a.count(a[i])
#         if(count == 1):
#             answer = a[i]
#         else:
#             continue
#     return answer

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     a = list(map(int, input().rstrip().split()))

#     result = lonelyinteger(a)

#     fptr.write(str(result) + '\n')

#     fptr.close()

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'flippingBits' function below.
# #
# # The function is expected to return a LONG_INTEGER.
# # The function accepts LONG_INTEGER n as parameter.
# #

# def flippingBits(n):
#     return (2**32 - 1) - n

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         n = int(input().strip())

#         result = flippingBits(n)

#         fptr.write(str(result) + '\n')

#     fptr.close()
# function oddOneOut(nums)
# {
#     nums.sort();
#     n = Math.max(nums)
#     for(i = 0; i < n+1; i++)
#     {
#         if (i != nums[i])
#         {
#             return i
#         }
#     }
# }
# console.log(oddOneOut([1,3,2,0,5]))