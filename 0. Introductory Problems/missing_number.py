n = int(input()) 
n_minus_1 = input()
arr = [int(item) for item in n_minus_1.split()]
def findMissingNumber(n, arr):
   ExpectedSum = n * (n + 1) // 2
   ArrSum = sum(arr)
   MissingNumber = ExpectedSum - ArrSum
   return MissingNumber
missing_number_result = findMissingNumber(n, arr)
print(missing_number_result)