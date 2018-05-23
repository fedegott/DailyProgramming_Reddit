
import os

base = '/Users/federicogottardo/Documents/Python/DailyProgramming_Reddit'

name_file = 'challenge350.rtf'

path = os.path.join(base,name_file)

with open(path,'r') as file: #file closed immediately after withxx as xxx: is closed. The "with" statement automatically closes the file  when the block ends.
    line = file.readlines()

shelves = line[9].split() #picks line number 9
# print(line[-1])

lines = str(line).split()

# for i in range(10,len(line)):
#     print( )
#     lines += line[i]
#     # lines.append(line[i])
# lines.split()
# # print(lines)
#

