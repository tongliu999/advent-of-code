import os
os.chdir('C:/advent-of-code/Day 1')
my_file = open("input.txt", "r") 
  
# reading the file 
data = my_file.read() 
  
# replacing end of line('/n') with ' ' and 
# splitting the text it further when '.' is seen. 
data_into_list = data.replace('\n', ' ').split() 

list_1 = []
list_2 = []

for i in range(0, len(data_into_list)): 
    if (i % 2 == 0):
        list_1.append(int(data_into_list[i]))

    else:  
        list_2.append(int(data_into_list[i]))

list_1.sort()
list_2.sort()

set_1 = set(list_1)

res = 0

for i in range(0, len(list_1)):
    multiplier = 0
    for j in range(0, len(list_2)):
        if list_2[j] == list_1[i]:
            multiplier += 1
    res += list_1[i] * multiplier

print(res)
my_file.close() 
