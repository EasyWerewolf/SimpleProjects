def input_convertor():
    #takes input and returns numeric value

    letter_grade = input('Enter a grade:\n ')

    if 'a' in letter_grade or 'A' in letter_grade:
        return 4.0
    elif 'b' in letter_grade or 'B' in letter_grade:
        return 3.0
    elif 'c' in letter_grade or 'C' in letter_grade:
        return 2.0        
    elif 'd' in letter_grade or 'D' in letter_grade:
        return 1.0
    elif 'f' in letter_grade or 'F' in letter_grade:
        return 0.0
    else:
        print('invalid input, please try again')
        input_convertor()
    return

def grad_status():

    grade_one = input_convertor()
    grade_two = input_convertor()
    grade_three = input_convertor()
    grade_four = input_convertor()

    final_result = ((grade_one + grade_two + grade_three + grade_four)/4)

    if final_result >=3.2 and final_result <=3.6:
        print('GPA is ' + str(final_result) + '\n Student can graduate cum laude')
    elif final_result >=3.6 and final_result <=3.8:
        print('GPA is ' + str(final_result) + '\n Student can graduate magna cum laude')
    elif final_result >=3.8 and final_result <=4.0:
        print('GPA is ' + str(final_result) + '\n Student can graduate summa cum laude')
    elif final_result >=2.0 and final_result <=3.2:
        print('GPA is ' + str(final_result) + '\n Student can graduate')
    else:
        print('Student is not eligble for graduation')


grad_status()



