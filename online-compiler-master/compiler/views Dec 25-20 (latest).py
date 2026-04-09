from django.shortcuts import render, redirect
from .forms import CodeAreaForm, InputsForm, CodeUploadForm #, SaveFileForm
from .models import CodeFileUpload
import subprocess
import os
import glob
import traceback
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.



##             If you ever copy
##               the    code
##                   or
##              even   whole
##               project (containing "Files Addresses" like, 'F:/django_projects/..../filename.ext' that is dependent on the previous folder or code file),
##             then   juest:
##  "make sure that you have change that 'Address', present in any code line of the file or project,
##      to the 'Current Folder Path' that you're currently in".




###     "Save Files" Button not showing "Modal" (solved).



# def login(request):

#     if not request.user.is_authenticated:

#         if request.method == 'POST':            

#             username = request.POST['uname']
#             password = request.POST['pwd']
#             user = auth.authenticate(username=username, password=password)

#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('home')
#             else:
#                 messages.info(request, 'Invalid Login Credentials!!')
#                 return redirect('/login/')                

#         else:
#             return render(request, 'compiler/login.html')

#     else:
#         return redirect('home')



# def login(request):    

#         if request.method == 'POST':            

#             username = request.POST['uname']
#             password = request.POST['pwd']
#             user = auth.authenticate(username=username, password=password)

#             if user is not None:
#                 auth.login(request, user)                
#             else:
#                 messages.info(request, 'Invalid Login Credentials!!')                

#             return redirect('home')              

#         else:
#             return render(request, 'compiler/base.html')    

































# def register(request):

#     if not request.user.is_authenticated:

#         if request.method == 'POST':

#             username = request.POST['username']
#             email = request.POST['email']
#             password1 = request.POST['password1']
#             password2 = request.POST['password2']

#             if password1 == password2:

#                 if User.objects.filter(username=username).exists():
#                     messages.info(request, 'This Username Already Exists!')
#                     return redirect('/register/')
                
#                 elif User.objects.filter(email=email).exists():
#                     messages.info(request, 'This Username Already Exists!')
#                     return redirect('/register/')

#                 else:
#                     user = User.objects.create_user(username=username, password=password1, email=email)
#                     user.save()
#                     print('\n\tUser Created!! \n\n')
#                     messages.info(request, 'User Created Successfully!!')
#                     return redirect('/login/')

#             else:
#                 messages.info(request, 'Two Passwords Do Not Match!!')
#                 return redirect('/register/')

#             return rediect('home')

#         else:
#             return render(request, 'compiler/register.html')            
    
#     else:
#         return render(request, 'base.html')












def logout(request):
    auth.logout(request)
    messages.success(request, 'Successfully Logged Out!!')
    return redirect('home')





def compile(request):

    compile_result = ''
    code_output = ''
    upload_context_flag = ''
    code = ''
    user_code = ''


    if request.user.is_authenticated:
        curr_user_id = str(request.user.id)
        user_files = CodeFileUpload.objects.all().filter(user_id__exact = curr_user_id)
    else:
        user_files = ['No', 'Files', 'Created', 'Yet', '!!']

    if request.method == 'POST':   

        ## For "Login" Authentification

        if not request.user.is_authenticated:

            if request.POST.get('uname') and request.POST.get('pwd'):
                username = request.POST['uname']
                password = request.POST['pwd']
                user = auth.authenticate(username=username, password=password)

                if user is not None:
                    auth.login(request, user)
                    messages.info(request, 'Logged In Successfully!!')                                     
                else:
                    messages.info(request, 'Invalid Login Credentials!!')      

            
            ## For "Sign-Up" Authentification

            if request.POST.get('username') and request.POST.get('email') and request.POST.get('password1') and request.POST.get('password2'):

                username = request.POST['username']
                email = request.POST['email']
                password1 = request.POST['password1']
                password2 = request.POST['password2']

                if password1 == password2:

                    if User.objects.filter(username=username).exists():
                        messages.info(request, 'This Username Already Exists!')                        
                    
                    elif User.objects.filter(email=email).exists():
                        messages.info(request, 'This Username Already Exists!')                        

                    else:
                        user = User.objects.create_user(username=username, password=password1, email=email)
                        user.save()
                        print('\n\tUser Created!! \n\n')
                        messages.info(request, 'User Created Successfully!!')                        

                else:
                    messages.info(request, 'Two Passwords Do Not Match!!')                    



        form = CodeAreaForm(request.POST)
        iform = InputsForm(request.POST) 
        upload = CodeUploadForm(request.POST, request.FILES)
        # savefile = SaveFileForm(request.POST)        

        print('\n\nPROG_LANG =', request.POST.get('prog_lang'), end = '\n\n')
        
        if form.is_valid() or upload.is_valid():                            

            try:                
                
                    ## If User tries to save the file...
                    # if savefile.is_valid():
                    #     if request.user.is_authenticated:                

                            # if request.POST.get('filename'):

                            #     print('\nUser ID :', request.user.id, end='\n\n')
                            #     print('\nFilename :', request.POST.get('filename'), end='\n\n')
                            #     print('\ncode (file save) :', code, end='\n\n')

                    #             # saving = CodeFileUpload.object.get()



                    if request.POST.get('filename'):

                        print('\nUser ID :', request.user.id, end='\n\n')
                        print('\nFilename :', request.POST.get('filename'), end='\n\n')
                        print('\ncode (file save) :', request.POST.get('code'), end='\n\n')                   
 
                    
                
                    ##   Getting Code and Inputs from Form Request.

                    if form.is_valid():
                        code_content = request.POST.get('code')

                        code = form.cleaned_data['code']  ## <--- When "POST" data is validated [required = True in forms.py(which, if nothing mentioned, is by default)]
                        code = code.split('\r\n')         
                        print('\n\nCode:\n', code, '\n')

                        if request.POST.get('filename'):

                            file_nm = request.POST.get('filename')   ## Getting the Name of the File.
                            file_nm = 'Code_Files/' + file_nm
                            file_object_pointer = open("%s/%s" %(settings.MEDIA_ROOT, file_nm),'w')   ## Opening the File (in a bit different way, i.e., by using Cpython Method) by using "Exact Address" where to store the file.        ####  Fully Correct   ####

                            for cd in code:    
                                file_object_pointer.write(cd)   ## Writing to the file that we just opened above.
                                file_object_pointer.write('\n')
                            file_object_pointer.close()   ## Now closing the same Opened File.

                            custom_upload = CodeFileUpload(codefile=file_nm, user_id=request.user.id)   ## Simply here, we are "manually giving the values" to our "model (CodeFileUpload)" object.
                            custom_upload.save()   ## Saving the model object.
                                ## So now, we get the user uploaded file into the desired "media/Code_Files/files" location along with assigning the "File to the Respected User".


                    elif upload.is_valid():

                        upload_context_flag = 1

                        obj = upload.save(commit=False)
                        obj.user = request.user
                        print('\nobj.CODEFILE :', obj.codefile.url, end='\n\n')
                        user_codefile = obj.codefile.url                                       
                        obj.save()
                        messages.success(request, 'File Uploaded Successfully..!!')

                        codefile_ref = 'F:/django_projects/online_compiler_beta4/media/Code_Files' + user_codefile

                        with open(codefile_ref, 'r') as f:                        
                            lines = f.readlines()

                            # code = []
                            user_code = ''
                            for line in lines:
                                user_code = user_code + line  

                            code = user_code.split('\n')                        
                            print('\nuser_code (upload) :', user_code, end='\n\n')
                            print('\nCode (upload) :', code, end='\n\n')
                            # code.append(line)
                            # code.append('\n')                                                    



                    if request.POST.get('inputs'):    ##  then data is retrived form "POST" request by "cleaned_data['']" method otherwise, Below method "request.POST.get('')" is used.
                        inputs = request.POST.get('inputs')  ## <--- This is for situations when data is not Validated-
                        inputs = inputs.split('\r\n')
                        # print('\nInputs:\n', inputs.split('\r\n'))
                    else:
                        inputs = ''            

                        
                    with open('inputs.txt', 'w') as fp:
                        for inp in inputs:
                            fp.write(inp)
                            fp.write('\n')
                    
                        


                    ##      For 'C' and "C++" Languages.            

                    if request.POST.get('prog_lang') == 'C' or request.POST.get('prog_lang') == 'C++':                                    

                        if request.POST.get('prog_lang') == 'C':
                            print('\n\nInitializing "C" - ("gcc") Compiler!\n\n')  ##
                            with open('program.c', 'w') as fp:
                                for cd in code:
                                    fp.write(cd)
                                    fp.write('\n')
                        else:
                            print('\n\nInitializing "C++" - ("g++") Compiler!\n\n')  ##
                            with open('program.c++', 'w') as fp:
                                for cd in code:
                                    fp.write(cd)
                                    fp.write('\n')

                        
                        if request.POST.get('prog_lang') == 'C':
                            subp = subprocess.Popen(['gcc', 'program.c'], shell=True, stderr=subprocess.PIPE)
                        else:
                            subp = subprocess.Popen(['g++', 'program.c++'], shell=True, stderr=subprocess.PIPE)
                        # compile_result = subp.stderr.read().decode('utf-8')
                        c = subp.stderr.read()

                        # " ".join(["{:02}".format(x) for x in c])  ## Nope :-(
                        # c = str(c)
                        # c = c[2:len(c)-1]
                        # c = c.split("\n")
                        # print('\n\n c =', c, end='\n\n\n' )            
                        # compile_result = c
                        

                        # if compile_result == b'':
                        if c == b'':            
                            subp = subprocess.Popen(['a.exe<inputs.txt'], shell=True, stdout=subprocess.PIPE)
                            code_output = subp.stdout.read().decode("utf-8") 
                            code_output = code_output.split('\r\n') ##
                            print('\nCode_Output =', code_output)  ##
                            compile_result = 'Great! No Errors..:-)'
                        else:
                            c = str(c)
                            c = c[2:len(c)-1]
                            c = str(c)
                            c = c.replace("\\n", "##").split("##")
                            print('\n\n c =', c, end='\n\n\n' )            
                            compile_result = c
                            code_output = 'Compilation Error...:-('
                            # print('\n Python3 err =', c, end='\n\n\n' )            
                            # compile_result = c.decode('UTF-8').split('\r\n')                    

                            # code_output = 'Compilation Error...:-('      




                    ##      For "Python_3" Language.

                    elif request.POST.get('prog_lang') == 'Python3':                                

                        print('\n\nInitializing "Python_3" Compiler!\n\n')
                        
                        with open('program.py', 'w') as fp:                        
                            for cd in code:
                                fp.write(cd)
                                fp.write('\n')                                                                            

                        
                        subp = subprocess.Popen(r'py F:/django_projects/online_compiler_beta4/program.py < F:/django_projects/online_compiler_beta4/inputs.txt', shell=True, stderr=subprocess.PIPE)
                        c = subp.stderr.read()

                        if c == b'':  

                            subp = subprocess.Popen(r'py F:/django_projects/online_compiler_beta4/program.py < F:/django_projects/online_compiler_beta4/inputs.txt', shell=True, stdout=subprocess.PIPE)
                            code_output = subp.stdout.read().decode("utf-8")
                            code_output = code_output.split('\r\n')
                            print('\nCode_Output =', code_output)

                            compile_result = 'Great! No Errors..:-)'                        

                        else:
                            print('\n Python3 err =', c, end='\n\n\n' )            
                            compile_result = c.decode('UTF-8').split('\r\n')                        

                            code_output = 'Compilation Error...:-('  

                            if compile_result.count('EOFError: EOF when reading a line') > 0:
                                # compile_result.append('\n')
                                compile_result.append('Probable Reason: Program requires some "input(s)" which is not provided. If it is so, please enter the input(s) in "Inputs(if any)" Textbox Field located above.')                       




                    ##      For "Java_1.8.0" Language.

                    elif request.POST.get('prog_lang') == 'Java':

                        print('\n\nInitializing "Java_1.8.0" Compiler!\n\n')
                        
                        with open('program.java', 'w') as fp:              
                            # for cd in code:        
                            #     fp.write(cd)
                            #     fp.write('\n')

                            temp_code = list(map(lambda x: x, code))
                            for i in range(len(temp_code)):
                                if 'public class' in temp_code[i]:    ## This is replaced below line because if ["program.java"] will contain ("public class")  then it will fail to execute becz we will need a "Java" File with the Filename of the "class" containing "main()" in given "code"
                                    temp_code[i] = temp_code[i].replace('public class', '/* Change: Removed "public class" */ class')

                                fp.write(temp_code[i])
                                fp.write('\n')


                        # fp = open('program.java', 'w')
                        # for cd in code:
                        #     fp.write(cd)
                        #     fp.write('\n')
                        # fp.close()                    


                        subp = subprocess.Popen(['javac', 'program.java'], shell=True, stderr=subprocess.PIPE)
                        c = subp.stderr.read()                

                        if c == b'':   ## This will be 'True' if Compilation gives "No Error".

                            class_files = glob.glob('*.class')   # Extracting (.class) File from Project Folder to get teh name of the ("class") containing ["main()"] in ["program.java"].
                            print('\n\nclass_files (list) :', class_files, end='\n\n')
                            # print('\n\n', , end='\n\n')                        

                            main_not_found_error_count = 0
                            c2_error_flag = ''
                            not_static_error_flag = ''    
                            empty_input_error = ''                

                            for c_file in class_files: 
                                                    
                                print('Class File Name :', c_file, end='\n\n')                                                   
                                class_file_name = c_file.replace('.class', '')
                                print('\n\nclass_file_name (replaced ".class")', class_file_name, end='\n\n')

                                class_file_name = class_file_name + '<inputs.txt'
                                print('\n\nclass_file_name (with "inputs.txt")', class_file_name, end='\n\n')

                                subp = subprocess.Popen(['java', class_file_name], shell=True, stderr=subprocess.PIPE)                         
                                c2 = subp.stderr.read().decode("utf-8")
                                print('\n\nc2 :', c2, end='\n\n')                        
                                print('\n\nc2 (type) :', type(c2), end='\n\n')   


                                # if c2 == '':
                                #     subp = subprocess.Popen(['java', class_file_name], shell=True, stdout=subprocess.PIPE)                         
                                #     code_output = subp.stdout.read().decode("utf-8")
                                #     code_output = code_output.split('\r\n')
                                #     print('\nCode_Output =', code_output, end='\n\n')
                                #     compile_result = 'Great! No Errors...:-)'

                                # else:
                                #     c2 = c2.replace('\n', '\n\n')
                                #     print("\nc2 (after replace) = ", c2, end='\n\n')
                                #     c2 = c2.split('\n')                                
                                #     compile_result = c2
                                #     print("\nc2 (after split) = ", compile_result, end='\n\n')
                                    
                                #     code_output = 'Compilation Error...:-('  

                                print('\nc2 (temp-no input) :', c2, end='\n\n')
                                if c2 != '':   ## If 'c2' is "not empty" string then it means there is "Some Error Message" received during compilation.

                                    c2_error_flag = 1  ## Signal Flag : 'c2_error_flag'

                                    if 'Error: Main method is not static' in c2:
                                        not_static_error_flag = 1
                                        break

                                    # elif 'error: invalid method declaration; return type required public static main(String args []) {' in c2:
                                    #     break                        

                                    elif 'Exception in thread "main" java.util.NoSuchElementException' in c2:
                                        empty_input_error = 1
                                        break        

                                    elif 'Error: Main method not found in class' in c2:
                                        main_not_found_error_count += 1                                

                                    else:
                                        break

                                else:
                                    c2_error_flag = 0                                
                                    break

                                # c2_error_flag = 0
                                print('\n-------------------------------------------------------------------------\n\n')



                            if c2_error_flag == 1:                            
                                
                                c2 = c2.replace('\n', '\n\n')
                                print("\nc2 (after replace) = ", c2, end='\n\n')
                                c2 = c2.split('\n')
                                # c2 = c2.split(': ')
                                compile_result = c2
                                print("\nc2 (after split) = ", compile_result, end='\n\n')                                                                                                                             

                                code_output = 'Compilation Error...:-('  


                                if main_not_found_error_count == len(class_files):                                
                                    compile_result = [
                                        'Error: Main method not found in any class of the program or not defined properly,',
                                        'please define the main method as:',
                                        '', 
                                        'public static void main(String[] args)',
                                        '',
                                        'or a JavaFX application class must extend javafx.application.Application'
                                    ] 
                                                                                                                    

                                elif empty_input_error == 1:
                                    # compile_result.append('\n')                       
                                    compile_result.append('Program requires for some "input(s)" which is not provided. If it is so, please enter the input(s) in "Inputs(if any)" Textbox Field located above.')                       

                                # else:   ## elif not_static_error_flag == 1:
                                    # c2 = c2.replace('\n', '\n\n')
                                    # print("\nc2 (after replace) = ", c2, end='\n\n')
                                    # c2 = c2.split('\n')
                                    # # c2 = c2.split(': ')
                                    # compile_result = c2
                                    # print("\nc2 (after split) = ", compile_result, end='\n\n')                                                                                                                             
                                                                

                                
                                
                            else:   ## elif c2_error_flag == 0:
                                subp = subprocess.Popen(['java', class_file_name], shell=True, stdout=subprocess.PIPE)
                                code_output = subp.stdout.read().decode("utf-8")
                                code_output = code_output.split('\r\n')
                                print('\nCode_Output =', code_output, end='\n\n')
                                compile_result = 'Great! No Errors..:-)'


                        else:   ## elif c != b'':
                            print('\n Java_1.8.0 err =', c, end='\n\n\n' )            
                            print('Java_1.8.0 type(err) =', type(c), end='\n\n\n' )            
                            compile_result = c.decode('UTF-8').split('\r\n')

                            if b'program.java:22: error: missing return statement\r\n   }\r\n   ^\r\n1 error\r\n' == c:
                                compile_result.append('\n')
                                compile_result.append("Probable Reason: Any return-type method not returning anything (no ''return'' statement in some method with return-type), make sure that 'main' method is properly defined as:")
                                compile_result.append('\n')
                                compile_result.append('public static void main(String[] args)')

                            code_output = 'Compilation Error...:-(' 



                        
                        class_files = glob.glob('*.class')
                        for c_file in class_files:
                            os.remove(c_file)    ## Deleting (.class) file as its work has been done (no longer in use).cd.
                            print("\nFile ['.class'] Removed !!\n")                    

                        
                        

                        ## ------------------------------------------------- ##





                        # class_file_name = class_file
                        # print('\n\nclass_file =', class_file_name, end='\n\n')

                        # class_file_name = class_file_name[0].replace('.class', '')   ## Removing ('.class') Extention from Filename [ "Hello.class" ---> "Hello" ]
                        
                        # java_file = class_file_name + '.java'   ## This will create a new file with the "(main)class" name [ like: Hello.java ]


                        # with open(java_file, 'w') as fp:
                        #     lines = fp.readlines()   ## This is done to copy the contents of the ["program.java"] file to ["actual_class_name.java"] file.
                        #     with open(java_file, 'w') as fp2:
                        #         for line in lines:
                        #             fp2.write(line)




                        ## ------------------------------------------------- ##




                        # with open(java_file, 'w') as fp:
                        #     for cd in code:
                        #         fp.write(cd)
                        #         fp.write('\n')
                                    

                        # if c == b'':          

                        #     # class_file = glob.glob('*.class')   # Extracting (.class) File from Project Folder                    

                        #     # class_file_name = class_file
                        #     # print('\n\nclass_file =', class_file_name, end='\n\n')

                        #     # class_file_name = class_file_name[0].replace('.class', '')   ## Removing ('.class') Extention from Filename [ "Hello.class" ---> "Hello" ]

                        #     # class_file_name = class_file_name + '<inputs.txt'
                        #     class_file_name = class_name
                        #     print('\n\nclass_file =', class_file_name, end='\n\n')

                        #     # subp = subprocess.Popen(['java', class_file_name], shell=True, stdout=subprocess.PIPE)
                        #     # code_output = subp.stdout.read().decode("utf-8")
                        #     # code_output = code_output.split('\r\n')
                        #     # print('\nCode_Output =', code_output, end='\n\n')
                        #     # compile_result = 'Great! No Errors..:-)'

                        #     subp = subprocess.Popen(['java', class_file_name], shell=True, stderr=subprocess.PIPE)
                        #     c2 = subp.stderr.read().decode("utf-8")

                        #     print("\n\nc2 = ", c2, end='\n\n')
                        #     print("\nc2 (type) =", type(c2), end='\n\n')                    

                        #     if c2 != '':
                        #         # c2 = c2.replace(':', '::')
                        #         c2 = c2.replace('\n', '\n\n')
                        #         print("\nc2 (after replace) = ", c2, end='\n\n')
                        #         c2 = c2.split('\n')
                        #         # c2 = c2.split(': ')
                        #         compile_result = c2
                        #         print("\nc2 (after split) = ", compile_result, end='\n\n')
                                
                        #         code_output = 'Compilation Error...:-('  
                        #     else:
                        #         subp = subprocess.Popen(['java', class_file_name], shell=True, stdout=subprocess.PIPE)
                        #         code_output = subp.stdout.read().decode("utf-8")
                        #         code_output = code_output.split('\r\n')
                        #         print('\nCode_Output =', code_output, end='\n\n')
                        #         compile_result = 'Great! No Errors..:-)'

                        #     class_file = class_file[0]
                        #     # class_file = 'F:/django_projects/Online_Compiler/' + class_file
                        #     # class_file = 'F:/django_projects/Online_Compiler/*.class'

                        #     # if os.path.isfile(class_file):
                        #     class_file = glob.glob('*.class')
                        #     for c_file in class_file:
                        #         os.remove(c_file)    ## Deleting (.class) file as its work has been done (no longer in use).cd.
                        #         print("\nFile ['.class'] Removed !!\n")

                        #     # java_file = 'F:/django_projects/Online_Compiler/' + java_file
                        #     # java_file = 'F:/django_projects/Online_Compiler/*.java'
                            
                        #     # if os.path.isfile(java_file):
                        #     java_file = glob.glob('*.java')
                        #     for j_file in java_file:
                        #         if j_file != 'program.java':
                        #             os.remove(j_file)
                        #             print("\nFile ['.java'] Removed !!\n")


                        # else:
                        #     print('\n Java_1.8.0 err =', c, end='\n\n\n' )            
                        #     compile_result = c.decode('UTF-8').split('\r\n')

                        #     code_output = 'Compilation Error...:-('  


            # except:
            except Exception as error:                    
                    # print(error)
                    compile_result = [ 'Something went wrong....', 'Internal Serval error: /', error, ' ', '"Please Try To Execute Again or Try After Somtime !!"', 'Our Team will be looking forward to re-solve this issue.', 'Sorry for the inconvinence this time :-<' ]
                    # compile_result = [ 'Something went wrong....', 'Internal Serval error: /', traceback.format_exc(), ' ', '"Please Try To Execute Again or Try After Somtime !!"' ]
                    code_output = 'Compilation Error...:-('

                    print('\n\nServer Error (type) :', type(error), end='\n\n')
                    print('\n\nServer Error (type) :', type(traceback.format_exc()), end='\n\n')
                    
                    with open('Error_log.txt', 'a') as f:

                        now = datetime.now()

                        curr_time = now.strftime('%I:%M %p')
                        curr_date = now.strftime('%d/%m/%Y')

                        server_error_time = '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tError at ' + curr_time + ' on ' + curr_date
                        print('\n\nServer Error Time : ', server_error_time, end='\n\n')

                        f.write('\n')
                        f.write(server_error_time)
                        f.write('\n')
                        # f.write(str(type(error)) + ': ' + str(error))
                        f.write(traceback.format_exc())
                        f.write('\n\n')
                

    else:
        form = CodeAreaForm()
        iform = InputsForm()
        upload = CodeUploadForm()
        # savefile = SaveFileForm()        


    print('\nupload_context_flag :', upload_context_flag, end='\n\n')
    if request.user.is_authenticated:
        context = { 'form': form, 'iform': iform, 'upload': upload, 'compile': compile_result, 'output': code_output, 'user_code': user_code, 'user_files': user_files }
    elif upload_context_flag == 1:
        context = { 'form': form, 'iform': iform, 'upload': upload, 'compile': compile_result, 'output': code_output, 'user_code': user_code, 'user_files': user_files }    
    else:
        context = { 'form': form, 'iform': iform, 'upload': upload, 'compile': compile_result, 'output': code_output, 'user_files': user_files }
    return render(request, 'compiler/base.html', context)
