from extract_from_transcript import *

courses = (extract_all_information())[2]
passed_courses = [course for course, is_true in courses if is_true]

math_course = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH","STAT"]


def count_math_courses(courses):
    count = 0
    for course_name in courses:
        subject = (course_name.split()[0])
        if subject in math_course:
            count = count + 1
    return count

# print(count_math_courses(passed_courses))


calculus_1 = ["MATH 116", "MATH 117", "MATH 127", "MATH 137", "MATH 147"]
calculus_2 = ["MATH 118", "MATH 119", "MATH 128", "MATH 138", "MATH 148"]
calculus_3 = ["MATH 237", "MATH 247"]
linear_algebra_1 = ["MATH 106", "MATH 136", "MATH 146"]
linear_algebra_2 = ["MATH 235","MATH 245"]

cs_1 = ["CS 115","CS 135","CS 145"]
cs_2 = ["CS 116", "136", "CS 146"]
stat_1 = ["STAT 230", "STAT 240"]
stat_2 = ["STAT 231", "STAT 241"]
extra = ["MATH 237", "MATH 239", "MATH 247", "MATH 249"]
algebra = ["MATH 135", "MATH 145"]

list_1 = ["EMLS 101R","EMLS 102R","EMLS 129R","ENGL 129R","ENGL 109","SPCOM 100","SPCOM 223"]
list_2 = ["EMLS 103R", "EMLS 104R", "EMLS 110R", "ENGL 108B", "ENGL 108D", "ENGL 119", "ENGL 208B","ENGL 209","ENGL 210E","ENGL 210F", "ENGL 378","MTHEL 300","SPCOM 225","SPCOM 227","SPCOM 228"]+list_1


table_1 = [list_1] + [list_2]
table_2 = [cs_1] + [cs_2] + [algebra] + [linear_algebra_1] + [linear_algebra_2] + [calculus_1] + [calculus_2] + [extra] + [stat_1] + [stat_2] 

ex_1 = ["EMLS 101R", "EMLS 110R"]
ex_2 = ["ENGL 108A"]
def table_1_check(courses):
    table_1_status = list(set(table_1[0]).intersection(set(courses)))
    if len(table_1_status) > 0:
        courses.remove(table_1_status[0])
    table_2_status = list(set(table_1[1]).intersection(set(courses)))
    if (len(table_1_status) > 0) and (len(table_2_status) > 0):
        return []
    if (len(table_1_status) == 0) and (len(table_2_status) == 0):
        return [list_1,list_2]
    if (len(table_1_status) > 0) and (len(table_2_status) == 0):
        return [list_2]
    if (len(table_1_status) == 0) and (len(table_2_status) > 0):
        return [list_1]

## Mathematical Studies
math_studies = [cs_1] + [cs_2] + [algebra] + [["MATH 106", "MATH 136", "MATH 146"]] + [["MATH 127", "MATH 137", "MATH 147"]] + [["MATH 128", "MATH 138", "MATH 148"]]
math_studies = math_studies + [["MATH 207","MATH 229","MATH 237","MATH 247","MATH 239","MATH 249"]]
math_studies = math_studies + [["MATH 225","MATH 235","MATH 245"]]
math_studies = math_studies + [["STAT 220","STAT 230","STAT 240"]]
math_studies = math_studies + [["STAT 221","STAT 231","STAT 241"]]


def math_studies_check(courses):
    cs1 = ["CS 115", "CS 135", "CS 145"]
    cs2 = ["CS 116", "CS 136", "CS 146"]
    alg = algebra
    lin_alg_1 = ["MATH 106", "MATH 136", "MATH 146"]
    lin_alg_2 = ["MATH 225","MATH 235","MATH 245"]
    calc_1 = ["MATH 127", "MATH 137", "MATH 147"]
    calc_2 = ["MATH 128", "MATH 138", "MATH 148"]
    calc_co = ["MATH 207","MATH 229","MATH 237","MATH 247","MATH 239","MATH 249"]
    stats_1 = ["STAT 220","STAT 230","STAT 240"]
    stats_2 = ["STAT 221","STAT 231","STAT 241"]
    if len(set(courses).intersection(set(cs1))) > 0:
        cs1 = []
    if len(set(courses).intersection(set(cs2))) > 0:
        cs2 = []
    if len(set(courses).intersection(set(alg))) > 0:
        alg = []
    if len(set(courses).intersection(set(lin_alg_1))) > 0:
        lin_alg_1 = []
    if len(set(courses).intersection(set(lin_alg_2))) > 0:
        lin_alg_2 = []
    if len(set(courses).intersection(set(calc_1))) > 0:
        calc_1 = []
    if len(set(courses).intersection(set(calc_2))) > 0:
        calc_2 = []
    if len(set(courses).intersection(set(calc_co))) > 0:
        calc_co = []
    if len(set(courses).intersection(set(stats_1))) > 0:
        stats_1 = []
    if len(set(courses).intersection(set(stats_2))) > 0:
        stats_2 = []
    ans = [cs1, cs2, alg, lin_alg_1, lin_alg_2, calc_1, calc_2, calc_co,stats_1,stats_2]
    filtered = [lst for lst in ans if lst]
    return filtered

print("Missing from list 1")
print(table_1_check(passed_courses))
print("Missing from list 2")
print(math_studies_check(passed_courses))

# ## Actuarial Science
# actuarial_science = [calculus_3] + ["AFM 101","ACTSC 231","ACTSC 232","ACTSC 331","ACTSC 371","ACTSC 431","ACTSC 446","AMATH 250","ECON 101","ECON 102","ENGL 378","MTHEL 300","MTHEL 131","STAT 330","STAT 331","STAT 333"]
# actuarial_science = actuarial_science + [["STAT 340", "STAT 341"]] + [["ACTSC 4XX","ACTSC 4XX"]]
# actuarial_science = actuarial_science + [["ACTSC 3XX", "ACTSC 4XX", "AFM 424", "STAT 431", "STAT 433", "STAT 441", "STAT 443", "MATH 3XX or 4XX"]]
# ## Need at least 26 Math courses

# ## Applied Mathematics
# applied_math = [calculus_3] + ["AMATH 231","AMATH 242","CS 371" ,"AMATH 251" ,"AMATH 332","AMATH 342","AMATH 351","AMATH","PHYS 121"]
# applied_math = applied_math + [["AMATH 4XX","AMATH 4XX","AMATH 4XX"]]
# applied_math = applied_math + [["AMATH 3XX","AMATH 4XX"]]
# applied_math = applied_math + [["5 math courses"]]
# # print(applied_math)
# ## Need at least 26 Math courses

