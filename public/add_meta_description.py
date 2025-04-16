import os
import yaml
import re
import textwrap

# Configuration
BASE_DIR = 'entradas/'  # Folder containing all post folders
MAX_LENGTH = 160
BACKUP_SUFFIX = '.bak'

def extract_description(text, max_length=160):
    """Extract the first meaningful sentence or paragraph and trim it for metadata."""
    match = re.search(r'(.{40,300}?[\.\!\?])', text, re.DOTALL)
    raw = match.group(1).strip().replace('\n', ' ') if match else text[:300].strip()
    return textwrap.shorten(raw, width=max_length, placeholder='')

def find_markdown_file(folder):
    """Return the first Markdown file inside a folder."""
    for file in os.listdir(folder):
        if file.endswith('.md'):
            return os.path.join(folder, file)
    return None

def update_description(filepath):
    """Update front matter with a description field if missing."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != '---':
        print(f"⚠️ No front matter in: {filepath}")
        return

    try:
        end_index = lines[1:].index('---\n') + 1
    except ValueError:
        print(f"⚠️ Front matter not closed properly in: {filepath}")
        return

    front_raw = ''.join(lines[1:end_index])
    body = ''.join(lines[end_index+1:]).strip()
    front = yaml.safe_load(front_raw)

    if 'description' not in front or not front['description']:
        description = extract_description(body)
        front['description'] = description

        # Backup and overwrite file
        os.rename(filepath, filepath + BACKUP_SUFFIX)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('---\n')
            yaml.dump(front, f, allow_unicode=True, sort_keys=False)
            f.write('---\n\n')
            f.write(body)

        print(f"✅ Added description to: {filepath}")
    else:
        print(f"✓ Already has description: {filepath}")

def batch_update_descriptions(base_dir):
    """Iterate through each folder inside `base_dir` and update description metadata."""
    for root, dirs, _ in os.walk(base_dir):
        for subfolder in dirs:
            folder_path = os.path.join(root, subfolder)
            md_file = find_markdown_file(folder_path)
            if md_file:
                update_description(md_file)

# Run the script
if __name__ == '__main__':
    batch_update_descriptions(BASE_DIR)
