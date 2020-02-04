#program1
"""
file_in = open("twotest.txt", "r")        
lines = file_in.readlines()
file_in.close()

file_out = open("delta.txt","w")
for index in range(0, len(lines)):
    file_out.write(lines[index])

file_out.close()


#program2
file_in = open("twotest.txt", "r") 
lines = file_in.readlines()
file_in.close()

file_out = open("delta.txt","w")
for index in range(0, len(lines), 2):
    file_out.write(lines[index])

file_out.close()
"""
#program3
file_in = open("twotest.txt", "r") 
lines = file_in.readlines()
file_in.close()

file_out = open("delta.txt","w")
for index in range(1, len(lines), 2):
    file_out.write(lines[index])

file_out.close()

