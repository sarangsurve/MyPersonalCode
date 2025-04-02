import re

def convert_to_markdown_table(markdown_text):
    sections = markdown_text.strip().split("***")
    
    rows = []
    for section in sections:
        lines = section.strip().split("\n")
        if lines:
            first_line = lines[0]
            match = re.match(r"\[(.*?)\]\((.*?)\)", first_line)
            if match:
                link_text, link_url = match.groups()
                formatted_text = f"[{link_text}]({link_url})" + "<br><br>" + "<br>".join(lines[1:]).strip()
                rows.append(f"| {formatted_text} |  |  |  |")
    
    table_header = "| Column 1 | Column 2 | Column 3 | Column 4 |\n"
    table_divider = "|----------|----------|----------|----------|\n"
    table_content = "\n".join(rows)
    
    return table_header + table_divider + table_content

# Example Markdown Input
markdown_input = '''
[AVS](https://localhost/AVS)

AVSawvga

wvawvae
ave

***

[XAU](https://localhost/XAU)

XAUawvga
eju
beab


ebvaeb
bewaab

***

[AVEB](https://localhost/AVEB)

AVEBawvga
abea
abeab

berbw
abe

***

[VKEIO](https://localhost/VKEIO)

VKEIOawvga

***

[VBAA](https://localhost/VBAA)

VBAAawvga
'''

# Generate and print the markdown table
markdown_table = convert_to_markdown_table(markdown_input)
print(markdown_table)
