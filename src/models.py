class Course:
    def __init__(self, title, description, instructor, duration):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"


contact_info = {
    "name": "Course Explainer Team",
    "email": "contact@courseexplainer.com",
    "address": "123 Learning Lane\nSuite 400\nSan Francisco, CA 94105",
    "social_links": [
        {"platform": "GitHub", "url": "https://github.com/courseexplainer"},
        {"platform": "LinkedIn", "url": "https://linkedin.com/company/courseexplainer"},
        {"platform": "Twitter", "url": "https://twitter.com/courseexplainer"},
    ],
}

courses = [
    Course("Introduction to Python",
           "Learn the basics of Python programming.", "John Doe", "4 weeks"),
    Course("Web Development with Flask",
           "Build web applications using Flask.", "Jane Smith", "6 weeks"),
    Course("Data Science Fundamentals",
           "An introduction to data science concepts and tools.", "Alice Johnson", "8 weeks"),
]
