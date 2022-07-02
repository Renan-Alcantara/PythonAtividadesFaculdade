num_tab = int(input('Digite um numero para ver sua tabuada: '))
nums = '1 2 3 4 5 6 7 8 9 10'.split()
print('---------------------------')
for num in nums:
  num = int(num)
  result = num * num_tab
  print(f'{num_tab} x {num} = {result}')
print('---------------------------')