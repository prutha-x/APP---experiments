import re


text = """
Hello,
Please contact us at python@example.com
or advanced@company.org.
"""

pattern = r'[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+'


emails = re.findall(pattern, text)

print("email addresses found:")
print(emails)
