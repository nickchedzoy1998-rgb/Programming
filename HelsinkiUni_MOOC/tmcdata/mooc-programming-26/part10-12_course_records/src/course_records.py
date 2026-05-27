# tee ratkaisusi tänne
class Course:
    def __init__(self, name, credits, grade):
        self.name = name
        self.credits = credits
        self.grade = grade

class Curriculum:
    def __init__(self):
        self.courses = {}

    def add_course(self, course: Course):
        self.courses[course.name] = course

    def get_stats(self):
        courses = len(courses)
        credits = 0

        for course in self.courses:
            credits += course.credits
        
        mean = credits / courses

        print(f'{courses} completed courses, a total of {credits} credits')
        print(f'mean {mean:.1f}')
        print('grade distribution')

        five = []
        four = []
        three = []
        two = []
        one = []

        for course in self.courses:
            if course.grade == 5:
                five.append('x')
            if course.grade == 4:
                four.append('x')
            if course.grade == 3:
                three.append('x')
            if course.grade == 2:
                two.append('x')
            if course.grade == 1:
                one.append('x')

        print(f'5: {five}')
        print(f'4: {four}')
        print(f'3: {three}')
        print(f'2: {two}')
        print(f'1: {one}')

class CourseRecordsApplication:
    def __init__(self):
        self.__curriculum = Curriculum()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")

    def add_course(self):
        course = input('course: ')
        grade = input('grade: ')
        self.__grades.add_course(course)

        print(course, grade)





    


    