
            ##
a = 'what?'

print(a)

a = a[len(a)-1:len(a)]

print(a)





            ##
import os
import subprocess

command = 'cmd'

os.system(command)

#  [OR]

#subprocess.Popen(command)


# command1 = r'cd C:\Users\Acer\AppData\Local\Programs\Python\Python38-32'
# os.system(command1)
# os.system(r'py C:\Users\Acer\AppData\Local\Programs\Python\Python38-32 hye.py')





            ##
import subprocess

subprocess.call(["gcc", "hello.c"])
subprocess.call("./a.exe");





            ##
import subprocess

print('Started...')

try:
    subprocess.call(["gcc", "hello.c"]) # This Will Compile The 'C' Code and
                                        #  will also return Compile Time Errors.
                                        
    subprocess.call("./a.exe") # This Will Run The 'C' Code and
                               #  will also return Output if No Compile Time
                               # Error is found.
    
except Exception as e:
    print('Console Error :', e)

finally:
    print('Done...!!')






            ##
a = 'a'
b = []

if type(a) == str and type(b) == list:
    print(type(a))
    print(type(b))
else:
    print('Types Not Matched!')






            ##
try:
    a = [1,2,3,4]
    b = 6
    b = a + b
    print(a)
    print(b)
    
except Exception as e:
    #print("Error:", e)
    err = e
    print("Error err:",err)
    b = a[0] + b +10
    print(a)
    print(b)
    print(e)









            ##
import traceback

try:
    a = [1,2,3,4]
    b = 6
    b = a + b
    print(a)
    print(b)
    
#except Exception as e:
except:    
    c = traceback.format_exc()    
    b = a[0] + b +10
    print(a)
    print(b)    
    print('\n\nDisplaying "Traceback" Error:\n\n', c)






