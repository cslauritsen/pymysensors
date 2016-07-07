import unittest

class Test2(unittest.TestCase):
	def test_lower(self):
		self.assertEqual('FOO'.lower(), 'foo')

