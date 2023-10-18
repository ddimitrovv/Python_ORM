# from django.test import TestCase
# from main_app.models import Student
# from caller import get_students_info, update_students_emails
#
#
# class StudentTestCase(TestCase):
#     def test_get_students(self):
#         Student.objects.create(
#             student_id="FC5204",
#             first_name="John",
#             last_name="Doe",
#             birth_date="1995-05-15",
#             email="john.doe@university.com",
#         )
#
#         Student.objects.create(
#             student_id="FE0054",
#             first_name="Jane",
#             last_name="Smith",
#             email="jane.smith@university.com",
#         )
#
#         Student.objects.create(
#             student_id="FH2014",
#             first_name="Alice",
#             last_name="Johnson",
#             birth_date="1998-02-10",
#             email="alice.johnson@university.com",
#         )
#
#         Student.objects.create(
#             student_id="FH2015",
#             first_name="Bob",
#             last_name="Wilson",
#             birth_date="1996-11-25",
#             email="bob.wilson@university.com",
#         )
#
#         students_info = get_students_info().strip()
#         self.assertEqual(students_info, """Student №FC5204: John Doe; Email: john.doe@university.com
# Student №FE0054: Jane Smith; Email: jane.smith@university.com
# Student №FH2014: Alice Johnson; Email: alice.johnson@university.com
# Student №FH2015: Bob Wilson; Email: bob.wilson@university.com""")
#
#
# class StudentTestCase(TestCase):
#     def test_get_students_info_practice_test(self):
#         Student.objects.create(
#             student_id="FC5204",
#             first_name="John",
#             last_name="Doe",
#             birth_date="1995-05-15",
#             email="john.doe@university.com",
#         )
#
#         Student.objects.create(
#             student_id="FE0054",
#             first_name="Jane",
#             last_name="Smith",
#             email="jane.smith@university.com",
#         )
#
#         Student.objects.create(
#             student_id="FH2014",
#             first_name="Alice",
#             last_name="Johnson",
#             birth_date="1998-02-10",
#             email="alice.johnson@university.com",
#         )
#
#         Student.objects.create(
#             student_id="FH2015",
#             first_name="Bob",
#             last_name="Wilson",
#             birth_date="1996-11-25",
#             email="bob.wilson@university.com",
#         )
#
#         update_students_emails()
#         expected_emails = ['john.doe@uni-students.com', 'jane.smith@uni-students.com', 'alice.johnson@uni-students.com', 'bob.wilson@uni-students.com']
#         actual_emails = [student.email for student in Student.objects.all()]
#         self.assertEqual(actual_emails, expected_emails)