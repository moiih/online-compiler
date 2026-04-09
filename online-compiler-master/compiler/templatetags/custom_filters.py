from django import template


register = template.Library()

@register.filter
def check_type(value):
    
    if type(value) == list:
        return 1
    else:
        return 0


@register.filter
def check_dir_address(line):

    if type(line) == str:
    
        dir_address = '  File "F:/django_projects/online_compiler_beta4/program.py"'
        if dir_address in line:
            return line.replace('  File "F:/django_projects/online_compiler_beta4/program.py"', 'File "./program.py"')
        else:
            return line
    else:
        return line


@register.filter
def first_letter_capital(string_value):

    string_value = str(string_value)

    if string_value[:1].islower():
        temp1 = string_value[1:]
        temp2 = string_value[:1].upper()

        # print('\nFirst Letter Question :', temp2+temp1, end='\n\n\n')
        return temp2 + temp1
    
    else:
        return string_value


@register.filter
def remove_file_address(file_url):

    file_url = str(file_url)

    if '/Code_Files/' in file_url:
        return file_url.replace('/Code_Files/', '')
    else:
        return file_url