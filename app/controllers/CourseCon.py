"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class CourseCon(Controller):
    def __init__(self, action):
        super(CourseCon, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Course')
        self.db = self._app.db
   
    def index(self):
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html', courses=courses)

    def add(self):
        course_details ={
            'title': request.form['courseName'],
            'description': request.form['description']
        }
        self.models['Course'].add_course(course_details)
        return redirect('/')

    def destroy(self, course_id):
        print "This is a destroy course_id;;;;;;;;;;"+ str(course_id)
        course =self.models['Course'].get_course_by_id(course_id)
        return self.load_view('destroy.html', course=course[0])
    
    def remove(self):
        course_id =request.form['courseId']
        noBtn = request.form['btn']
        if noBtn != "No":
            print "This is a controller course_id;;;;;;;;;;"+ course_id
            self.models['Course'].delete_course(course_id)
        return redirect('/')