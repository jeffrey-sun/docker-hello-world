# -*- coding:utf-8 -*-

from nose.tools import assert_equal 

def setUp():
	print "==== python nose unittest demo module begin ==="

def test_add():
	print "=== test_add ==="
	result = 4 + 5
	assert_equal(result, 9)

class TestClass(object):
	def __init__(self):
		pass

	def setUp(self):
		print "=== TestClass setUp ==="

	def  tearDown(self):
		print "=== TestClass tearDown ==="

	def test_evens(self):
		for i in range(0, 5):
			yield self.check_even, i, i*3

	def check_even(self, n, nn):
		assert n % 2 ==0 or nn % 2 == 0

	def test_add(self):
		result = 4 + 5
		assert_equal(result, 9)


		