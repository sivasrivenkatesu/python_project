'''import sys

# Check if arguments are provided
if len(sys.argv) < 2:
    print("Usage: python script.py <arg1> <arg2> ...")
    sys.exit(1)

# Print the number of arguments passed
print("Number of arguments:", len(sys.argv))

# Print all the arguments passed
print("Arguments:", sys.argv)

# Access individual arguments
print("First argument:", sys.argv[0])
print("Second argument:", sys.argv[1])  # Note: Index 0 is the script name
'''

import sys
print(sys.argv)
print(len(sys.argv))
a=int(sys.argv[1])
b=int(sys.argv[2])
print("Addition:",a+b)
file=open("output.txt.txt","r+")

wordcount={}
for word in file.read().split():
     if word not in wordcount:
          wordcount[word]=1
     else:
         wordcount[word]+=1
import sys
print(sys.argv)
print(len(sys.argv))
a=int(sys.argv[1])
b=int(sys.argv[2])
print("Addition:",a+b)
file=open("output.txt.txt","r+")

wordcount={}
for word in file.read().split():
     if word not in wordcount:
          wordcount[word]=1
     else:
         wordcount[word]+=1
import sys
print(sys.argv)
print(len(sys.argv))
a=int(sys.argv[1])
b=int(sys.argv[2])
print("Addition:",a+b)
file=open("output.txt.txt","r+")

wordcount={}
for word in file.read().split():
     if word not in wordcount:
          wordcount[word]=1
     else:
         wordcount[word]+=1
for word, count in wordcount.items():
            print(f"{word}: {count}")
file.close()

