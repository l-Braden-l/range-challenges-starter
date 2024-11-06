#Braden Leach
#Nov 6 2024
#Range challenges




#Counting Up & Down

    #input
number_i = int(input('Please input an integer: '))

#counting up 
for num in range(1,number_i + 1):
 print(num)

#counting down
for num2 in range(number_i,0,-1):
 print(num2)

print(f'We have lift off!')


#Number Cubes
for number in range(1,10): 
   result = number ** 3
   print(f'The cube of {number} is {result} ')

#Multiplication Table

number = 7 
for num in range(1,10):
  mulit = number * num
  print(f' {number} X {num} = {mulit}')

#List Iteration
total = 0
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
num_elements = len(numbers)

for i in range(num_elements):
  total += numbers[i]

print(f'The sum of the numbers in my list is {total}')