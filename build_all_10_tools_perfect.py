import re
import os
import shutil

print("Step 1: Reading existing files...")

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    script_js = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

print(f"Read index.html ({len(index_html)} bytes), script.js ({len(script_js)} bytes), style.css ({len(style_css)} bytes)")
