#This is just to rename the files in proper order or random order depending upon the requirement
import os
import random
import sys

def rename_all(path,f):
    for i in range(1,f,-1):
        random_number=random.randrange(1500,3000)*i
        for file in os.listdir(path):
            if file.endswith('.wav'):
                os.rename(path+'\\'+file,path+'\\'+str(random_number)+'.wav')
                random_number+=1

arguments=sys.argv
print(arguments[-1])
f=[0 if arguments[-1]=='random' else -1]
print(f)
rename_all(input('Enter Path of the file: '),f[0])
