from flask import render_template
from models import contact_info, courses


def index():
    return render_template('index.html', courses=courses)


def course(course_id):
    course = courses[int(course_id) - 1]
    return render_template('course.html', course=course, course_id=course_id)


def contact():
    return render_template('contact.html', contact=contact_info)
