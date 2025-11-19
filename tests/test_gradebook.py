# tests/test_gradebook.py
"""
Basic tests for gradebook functions.
"""

from gradebook.gradebook import average, curve, letter_grade
def test_average_basic():
    assert average([100, 80, 90]) == 90.0
def test_average_empty():
    assert average([]) == 0.0
def test_curve_basic():
    assert curve([70, 80, 90], 5) == [75, 85, 95]
def test_letter_grade_basic():
    assert letter_grade(95) == "A"
    assert letter_grade(85) == "B"
    assert letter_grade(75) == "C"
    assert letter_grade(65) == "D"
    assert letter_grade(50) == "F"