from gradebook.gradebook import average, curve, letter_grade


def test_average():
    assert average([100, 80, 60]) == 80.0
    assert average([]) == 0.0


def test_curve():
    assert curve([80, 90], 5) == [85, 95]


def test_curve_negative():
    assert curve([10, 20], -15) == [0, 5]
    assert curve([10, 20], -15, allow_negative=True) == [-5, 5]


def test_letter_grade():
    assert letter_grade(95) == "A"
    assert letter_grade(85) == "B"
    assert letter_grade(75) == "C"
    assert letter_grade(65) == "D"
    assert letter_grade(50) == "F"