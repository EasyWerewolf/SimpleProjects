class BusinessCard():

    def get_input():
        first_name = input('Enter First Name: ')
        last_name = input('Enter Last Name: ')
        student_email = input('Enter email address: ')
        return first_name, last_name, student_email

    def print_output(first_name, last_name, student_email):
        print(first_name + ' ' + last_name)
        print('Student')
        print(student_email)
        print('Community College of Philadelphia')
        print('1700 Spring Garden St.')
        print('Philadelphia PA 19130')

    get_input()
    