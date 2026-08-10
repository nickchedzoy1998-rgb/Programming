# Attempted courses

> **NB:** Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing **Submit Solution** from the menu next to the button for executing tests.

The exercise template contains the class definition for a `CourseAttempt`. It works like this:

```python
attempt = CourseAttempt("Peter Python", "Introduction to Programming", 5)
print(attempt.student_name)
print(attempt.course_name)
print(attempt.grade)
print(attempt)
```

**Sample output**

```text
Peter Python
Introduction to Programming
5
Peter Python, grade for the course Introduction to Programming 5
```

## Names of students

Please write a function named `names_of_students(attempts: list)` which takes a list of `CourseAttempt` objects as its argument. The function should return a new list with the names of the students who have attempted the course.

```python
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in names_of_students([s1, s2, s3]):
    print(name)
```

**Sample output**

```text
Peter Python
Olivia C. Objective
Peter Python
```

Please implement the function using the `map` function.

## Courses

Please write a function named `course_names(attempts: list)` which takes a list of `CourseAttempt` objects as its argument. The function should return a new list containing the names of the courses on the original list in alphabetical order. Each course name should appear only once on the list.

```python
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in course_names([s1, s2, s3]):
    print(name)
```

**Sample output**

```text
Advanced Course in Programming
Introduction to Programming
```

Please implement the function using the `map` function. That alone will likely not be enough, however. You will need something else, too, to make sure the course names are unique.
