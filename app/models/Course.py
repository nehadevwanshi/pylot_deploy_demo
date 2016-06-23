from system.core.model import Model
class Course(Model):
	def __init__(self):
		super(Course, self).__init__()

	def get_all_courses(self):
		return self.db.query_db("SELECT * FROM courses")
    
	def add_course(self, course):
		query = "INSERT INTO courses (title, description, created_at) VALUES (:title, :description, NOW())"
		data = { 'title': course['title'], 'description': course['description'] }
		return self.db.query_db(query, data)

	def delete_course(self, course_id):
		query= "DELETE FROM courses WHERE id =:course_id"
		data = { "course_id": course_id }
		print "This is a course_id;;;;;;;;;; " + course_id
		return self.db.query_db(query, data)

	def get_course_by_id(self, course_id):
		data = { "course_id": course_id }
		return self.db.query_db("SELECT * FROM courses WHERE id=:course_id", data)