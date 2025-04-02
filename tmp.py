import re

def transform_text(line: str) -> str:
    # Replace special characters except underscore, hyphen, and whitespaces with empty string
    line = re.sub(r"[^a-zA-Z0-9_\-\s]", "", line)
    # Replace all whitespaces with hyphen
    line = re.sub(r"\s+", "-", line)
    return line

content = """XXXXXX"""
# content = input("Enter the content: ")

new_content = """"""
for line in content.splitlines():
    # Skip empty lines
    if not line.strip():
        continue
    # Transform the line
    transformed_line = transform_text(line)
    new_content += transformed_line + "\n"

print(new_content)
