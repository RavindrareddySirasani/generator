iter=iter([1,2,3,4])
'''print(iter)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))


output
------
<list_iterator object at 0x0000029BCB0B2470>
1
2
3
4
Traceback (most recent call last):
  File "C:/Users/HP/Documents/generator/generator.py", line 7, in <module>
    print(next(iter))
StopIteration
'''
for i in iter:
    print(i)

'''
output
------------
1
2
3
4
iterator looks like for loop. implement iteratoe use iter keyword and next keyword.
'''
##while True:
##    try:
##        print(next(iter1)
##    except StopIteration:
##              break
              
