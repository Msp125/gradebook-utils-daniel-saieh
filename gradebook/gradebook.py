# gradebook/gradebook.py
"""
Gradebook utility functions for operting grades (computing, sorting, etc.).
"""
def average(scores):
    """Compute the average of a list of scores."""
    return sum(scores) / len(scores) if scores else 0.0
def curve(scores, points):
    """Return a new list of scores after adding `points` to each."""
    return [s + points for s in scores]
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