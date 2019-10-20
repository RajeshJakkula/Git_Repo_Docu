# Seek() and tell() methods in python
#using tell() we can know the position of the cursor in file
#using seek() we can move cursor back and set the position where ever you want.
#seek(offset, from_what_pos)
#opening file
fb=open('/Users/rajeshjakkula/Documents/Pycharm_Pythoncode/Data_set/cursor_file.txt','r')
# knowing the current position
print(fb.tell())
#0, is my current positon
print(fb.readline()) # reading first line from file
#Apple
print(fb.tell()) # then knowing the position
#6
print(fb.readline()) # reading 3 to four lines
#Facebook
print(fb.readline())
#Google
print(fb.tell()) # and then knowing the position
#22
print(fb.seek(0,0)) # setting back position where i started
#0
print(fb.tell()) # then knowing the position
#0
print(fb.readline())
#Apple
print(fb.seek(1)) # setting position from onwards, in my file Apple is first line i want to skip in the line and start the cursor from p onwards
#1
print(fb.readline()) # Data
#pple
print(fb.readline())
#Facebook
print(fb.readline())
#Google
print(fb.readline())
#Amazon
print(fb.readline())
#Uber
print(fb.seek(10,0)) # here setting position from 10 onwards, that means starts from second line letter 10 onwards include first line space
#10
print(fb.tell())
#10
print(fb.readline())
#book
print(fb.seek(0,1)) # knowing the current position
#15
print(fb.seek(0,2)) # knowing the number of position available in file including each line space.
#99
