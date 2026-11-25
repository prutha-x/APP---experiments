# Decorator to convert output to uppercase
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


class Report:
    def __init__(self, title):
        self.title = title

    @classmethod
    def from_template(cls, template):
        return cls(template)

    def __str__(self):
        return f"Report Title: {self.title}"

    @uppercase_decorator
    def generate(self):
        return f"This is the report: {self.title}"


# Main Program
title = input("Enter the report title: ")

report = Report.from_template(title)

print("\n", report)
print(report.generate())
