```python
#count dup letters
def counter(s):
  l = list(s)
  contains = []
  dups =[]
  for i in range(len(l)):
    if not l[i] in contains:
      contains.append(l[i])
    else:
      if not i in dups:
        dups.append(l[i])
  return dups


print(counter("aabbcde"))
```
_*Q5*_
```python
#non consecutive
def check(l):
  check_count = l[0]
  for i in range(len(l)):
    if check_count != l[i]:
      return None #null?
    else:
      check_count +=1
  return("Array is consecutive")
  
  
lst = [-4,-3,-1,0,1,2,3,4,5,6,7,8]
print(check(lst))
```

