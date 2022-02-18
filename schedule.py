'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def title(self,phrase):
        ''' title returns the courses that contain the search phrase'''
        return Schedule([course for course in self.courses if phrase.lower() in course['name'].lower()])

    def status(self,status,consent):
        ''' status returns courses with a particular enrollment status'''
        if consent:
            return Schedule([course for course in self.courses if status.lower() in course['status_text'].lower() and "consent" in course['status_text'].lower()])
        else:
            return Schedule([course for course in self.courses if status.lower() in course['status_text'].lower() and "consent" not in course['status_text'].lower()])

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def limit(self,lim):
        ''' returns the courses that have a greater than or equal to inputted limit amount of students able to enroll'''
        return Schedule([course for course in self.courses if course['limit']>=lim])

    def independent_study(self,independent_study):
        ''' subject filters by whether or not independent study '''
        return Schedule([course for course in self.courses if course["independent_study"] == independent_study])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def description(self,phrase):
        ''' subject filters the courses by description '''
        return Schedule([course for course in self.courses if phrase in course["description"]])

    def sort(self,field):
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        else:
            print("can't sort by "+str(field)+" yet")
            return self

    def num(self,vals):
        return Schedule([course for course in self.courses if course['coursenum'] in vals])
