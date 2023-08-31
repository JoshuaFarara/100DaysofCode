fruits = ['apple', 'orange', 'apple']

def count_fruits(fruits):
  '''
  input: ['apple', 'orange', 'apple']
  output: {'apple':2, 'orange':1}
  '''
  out = {}
  for fruit in fruits:
    if fruit not in out:
      out[fruit] = 1
    else:
      out[fruit] += 1
    return out