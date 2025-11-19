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

def test_curve_basic():
    assert curve([70, 80, 90], 5) == [75, 85, 95]
def test_curve_clamps_to_zero_on_negative_results():
    # Penalize: some scores would go negative → clamp to 0
    assert curve([10, 3, 0], -5) == [5, 0, 0]
    # Already-negative inputs: small positive curve still clamps
    assert curve([-2], 1) == [0]
    # Positive curve still behaves as before
    assert curve([70, 80, 90], 5) == [75, 85, 95]


    # If points to be curved are not allowed to be negative
    assert curve([30, 40, 50], -5, False) == [30, 40, 50]

