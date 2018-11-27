#Print 1 3 6 10 15 21  (1 1+2 1+2+3 1+2+3+4 1+2+3+4+5 1+2+3+4+5+6) Using Recursion

def MyRecur(k):
  if(k>0):
    result = k + MyRecur(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Completed, Results: ")
MyRecur(6)