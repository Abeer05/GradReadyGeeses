import re
from pypdf import PdfReader


        
def get_all_lines(path):
    output = []
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)

    for i in range(number_of_pages):

        page = reader.pages[i]
        text = page.extract_text(extraction_mode = 'plain').splitlines()
        output.extend(text)
    return output

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def check_is_couse_row(row):
    word_list = row.split(" ")
    if (word_list[0].isupper() and is_number(word_list[-2]) and is_number(word_list[-3])):
        return True
    return False
def extract_couse_info(row):
    word_list = row.split()
    status = word_list[-1]
    is_pass = False
    if (is_number(status)):
        is_pass = float(status) >= 50
    elif (status == 'CR'):
        is_pass = True
    return (word_list[0] + ' ' +  word_list[1], is_pass)
def check_is_name(row):
    return 'Name:' in row
def check_is_program(row):
    return 'Program:' in row
def extract_name_or_program(row):
    return ''.join(row.split()[1:])
def extract_all_information(path):
    output_lines = get_all_lines(path)
    course_map = {}
    name = ''
    program = ''
    for row in output_lines:
        if check_is_program(row):
            program = extract_name_or_program(row)
            continue
        if check_is_name(row):
            name = extract_name_or_program(row)
            continue
        if check_is_couse_row(row):
            course_info = extract_couse_info(row)
            course_map[course_info[0]] = course_info[1]
            
            continue
    
    return(name, program,list(course_map.items()))


