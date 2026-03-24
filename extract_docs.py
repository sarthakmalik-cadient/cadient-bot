import zipfile
import xml.etree.ElementTree as ET
import os

def get_docx_text(path):
    """
    Extract text from a .docx file.
    """
    try:
        with zipfile.ZipFile(path) as z:
            xml_content = z.read('word/document.xml')
        
        tree = ET.fromstring(xml_content)
        text = ''
        for node in tree.iter():
            if node.tag.endswith('t'):
                text += node.text if node.text else ''
            elif node.tag.endswith('p'):
                text += '\n'
        return text
    except Exception as e:
        return f"Error reading {path}: {e}"

docs_dir = r"D:\Documents\PycharmProjects\cadient chat bot\docs"
output_file = r"D:\Documents\PycharmProjects\cadient chat bot\docs_summary_raw.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for filename in os.listdir(docs_dir):
        if filename.endswith(".docx"):
            path = os.path.join(docs_dir, filename)
            # print(f"Processing {filename}...")
            f.write(f"--- FILE: {filename} ---\n")
            f.write(get_docx_text(path))
            f.write("\n\n")

print(f"Done. Output saved to {output_file}")
