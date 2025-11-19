# gradebook/gradebook.py
"""
Gradebook utility functions for operating grades (computing, sorting, etc.).
"""


def average(scores):
    """Compute the average of a list of scores."""
    return sum(scores) / len(scores) if scores else 0.0


def curve(scores, points, allow_negative=False):

def curve(scores, points, negative_points_allowed=True):
    """
    Return a new list of scores after adding `points` to each.
    If allow_negative is False, scores are clamped at a minimum of 0.
    """

    if allow_negative:
        return [s + points for s in scores]
    return [max(0, s + points) for s in scores]


def letter_grade(score):
    """Return a letter grade (A, B, C, D, F) for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

    if not negative_points_allowed and points < 0:
        points = 0
    return [max(0, s + points) for s in scores]
