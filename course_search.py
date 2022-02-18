'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
status (filter by current course status, e.g. Closed, or Open Consent Req.)
independent study (filter by whether or not a course is an independent study)
coursenum (filter by coursesnum, e.g 240f)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        elif command in ['title']:
            title = input("enter a title:")
            schedule = schedule.title(title)
        elif command in ['description']:
            phrase = input("enter a phrase:")
            schedule = schedule.description(phrase)
        elif command in ['de','details']:
            det = input("enter a detail of a course: ")
            schedule = schedule.details(det)
        elif command in ['status']:
            status = input("enter a status (open/closed):")
            consent = input("consent required? (yes/no):")
            if consent == "yes":
                schedule = schedule.status(status, True)
            else:
                schedule = schedule.status(status, False)
        elif command in ['instructor']:
            flag = input("email or lastname ?")
            if flag == "email":
                query = input("Please enter the email:")
                schedule = schedule.email(query)
            else:
                query = input("Please enter the instructor's lastname:")
                schedule = schedule.lastname(query)
        elif command in ['is', 'independent study']:
            is_independent_study = input("independent study? (y/n):")
            if is_independent_study == "y":
                schedule = schedule.independent_study(True)
            elif is_independent_study == "n":
                schedule = schedule.independent_study(False)
        elif command in ['num']:
            query = input("Please enter the courses of the day you want to query:")
            schedule = schedule.num(query)
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()
