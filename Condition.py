# UGC Uniform Grading System

marks = int(input('Enter marks: '))

if marks <= 100 and marks >= 80:
    print(f'Your grade is: A+')
elif marks < 80 and marks >= 75:
    print(f'Your grade is: A')
elif marks < 75 and marks >= 70:
    print(f'Your grade is: A-')
elif marks < 70 and marks >=65:
    print(f'Your grade is: B+')
elif marks < 64 and marks >=60:
    print(f'Your grade is: B')
elif marks < 60 and marks >=55:
    print(f'Your grade is: B-')
elif marks < 55 and marks >=50:
    print(f'Your grade is: C+')
elif marks < 50 and marks >=45:
    print(f'Your grade is: C')
elif marks < 45 and marks >=40:
    print(f'Your grade is: D')
elif marks < 40 and marks >=0:
    print(f'Your grade is: F')
