import re
import os
import shutil

print("Updating build_full_suite.py with accessible, bulletproof label dropzones...")

with open('build_full_suite.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Pattern to replace dropzone div with label
def replacer(match):
    dropzone_id = match.group(1)
    input_id = match.group(2)
    full_block = match.group(0)
    
    # Replace opening div with label
    new_block = full_block.replace(
        f'<div class="file-dropzone" id="{dropzone_id}" onclick="document.getElementById(\'{input_id}\').click()">',
        f'<label class="file-dropzone" id="{dropzone_id}" for="{input_id}">'
    )
    # Replace closing div for the dropzone
    # Note that full_block ends with </div>
    last_div_idx = new_block.rfind('</div>')
    if last_div_idx != -1:
        new_block = new_block[:last_div_idx] + '</label>' + new_block[last_div_idx + 6:]
    
    # Remove onclick="event.stopPropagation(); this.value = null;" and style="display:none;"
    new_block = re.sub(r'style="display:none;"\s*', 'class="visually-hidden-file-input" ', new_block)
    new_block = re.sub(r'onclick="event\.stopPropagation\(\);\s*this\.value\s*=\s*null;"\s*', '', new_block)
    
    return new_block

pattern = re.compile(r'<div class="file-dropzone" id="([^"]+)" onclick="document\.getElementById\(\'([^\']+)\'\)\.click\(\)">\s*<input[^>]+>[\s\S]*?</div>')

code_new, count = pattern.subn(replacer, code)
print(f"Replaced {count} dropzones in build_full_suite.py.")

with open('build_full_suite.py', 'w', encoding='utf-8') as f:
    f.write(code_new)

print("Running build_full_suite.py...")
import subprocess
res = subprocess.run(['python3', 'build_full_suite.py'], capture_output=True, text=True)
print("build_full_suite output:", res.stdout)
if res.stderr:
    print("build_full_suite error:", res.stderr)

