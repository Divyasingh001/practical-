#Count tuples occurrence in list of tuples
import collections 
Output = collections.defaultdict(int)
Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')],
         [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]
for elem in Input:
      Output[elem[0]] += 1
print(Output)
