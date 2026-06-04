from flask import render_template
from models import contact_info


def index():
    return render_template('index.html')


def course(course_id):
    return render_template('course.html', course_id=course_id)


def contact():
    return render_template('contact.html', contact=contact_info)
