
#GETTING COURSE AND PRINTING THE COURSE OF A STUDENT USING IF-ELIF-ELSE STATEMENT
name=input("ENTER YOUR NAME:")
year=input("ENTER THE YEAR OF JOINING:")
code=input("ENTER YOUR COURSE CODE:")# CS=239 AND IT=242
s_number=input("ENTER YOUR SERIAL NUMBER:")
roll_number=year+code+s_number
if code=="239":
    print("NAME:",name)
    print("ROLL NUMBER:",roll_number)
    print("COURSE:COMPUTER SCIENCE")
elif code=="242":
    print("NAME:", name)
    print("ROLL NUMBER:", roll_number)
    print("COURSE:INFORMATION TECHNOLOGY")
else:
    print("NAME:", name)
    print("ROLL NUMBER:", roll_number)
    print("INVALID COURSE CODE!!!!!!!!!!!")

#---------------------------------------------------------------
#OUTPUT
'''
#INFORMATION TECHNOLOGY
ENTER YOUR NAME:KAMALINI
ENTER THE YEAR OF JOINING:2021
ENTER YOUR COURSE CODE242
ENTER YOUR SERIAL NUMBER:001
NAME: KAMALINI
ROLL NUMBER: 2021242001
COURSE:INFORMATION TECHNOLOGY

#COMPUTER SCIENCE
ENTER YOUR NAME:KAMALINI
ENTER THE YEAR OF JOINING:2021
ENTER YOUR COURSE CODE:239
ENTER YOUR SERIAL NUMBER:003
NAME: KAMALINI
ROLL NUMBER: 2021239003
COURSE:COMPUTER SCIENCE

#INVALID OUTPUT
ENTER YOUR NAME:KAMALINI
ENTER THE YEAR OF JOINING:2021
ENTER YOUR COURSE CODE:245
ENTER YOUR SERIAL NUMBER:010
NAME: KAMALINI
ROLL NUMBER: 2021245010
INVALID COURSE CODE!!!!!!!!!!!

'''
