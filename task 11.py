# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

a = int(input())
a0 = 0
a1 = 0
a2 = 1
i = 2 # Так как 2 первых числа уже известны это 0 и 1

while a0 < a:
   a0 = a1 + a2
   a1 = a2
   a2 = a0
   i += 1
   if a0 > a:
     i = 0
if i != 0:
  print(i)      
else:
  print(-1)