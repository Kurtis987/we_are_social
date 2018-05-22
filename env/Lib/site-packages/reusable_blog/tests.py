from django.test import TestCase
from .models import Post

# Create your tests here.
class PostTests(TestCase):
	"""
	define tests to run against the Post model
	"""
	def test_str(self):
		test_title = Post(title='My Latest Blog Post')
		self.assertEqual(str(test_title.title),
						'My Latest Blog Post')