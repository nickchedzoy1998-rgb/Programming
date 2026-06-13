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

    def get_course(self, course:str):
        return self.courses.get(course)

    def get_stats(self):
        courses = len(self.courses)
        credits = 0
        grades = 0

        for c in self.courses.values():
            grades += int(c.grade)
            credits += int(c.credits)
        
        if courses == 0:
            print('no courses to generate stats from')
            return
        
        mean = grades / courses

        print(f'{courses} completed courses, a total of {credits} credits')
        print(f'mean {mean:.1f}')
        print('grade distribution')

        all_grades = [c.grade for c in self.courses.values()]

        for grade in ['5', '4', '3', '2', '1']:
            count = all_grades.count(grade)
            print(f'{grade}: {"x" * count}')

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
        credits = input('credits: ')

        if self.__curriculum.get_course(course) is None:
            obj = Course(course, credits, grade)
            self.__curriculum.add_course(obj)
            return
        
        existing_course = self.__curriculum.get_course(course)
        current_grade = existing_course.grade

        if int(grade) > int(current_grade):
            existing_course.grade = grade
            return

        

    def get_course_data(self):
        course = input('course: ')

        course_object = self.__curriculum.get_course(course)

        if course_object is None:
            print('no entry for this course')
            return
        
        else:
            print(f'{course} ({course_object.credits} cr) grade {course_object.grade}')
        
    def statistics(self):
        self.__curriculum.get_stats()

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == '3':
                self.statistics()
            else:
                self.help()


application = CourseRecordsApplication()
application.execute()