import unittest

import hello_funs

class HelloFunsTests(unittest.TestCase):

    def test_say_something_to_someone(self):
        self.assertEqual(hello_funs.say_something_to_someone("Yo", "Bob"), "Yo Bob")
        self.assertEqual(hello_funs.say_something_to_someone("", ""), " ")
