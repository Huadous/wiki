import os
import re

def fix_tags_in_file(filepath):
    """Convert YAML tags from flow sequence [...] to block style if they contain problematic chars"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return False
    
    frontmatter = fm_match.group(1)
    
    # Find tags: [...] lines
    tag_line_match = re.search(r'^tags:\s*\[(.*?)\]', frontmatter, re.MULTILINE)
    if not tag_line_match:
        return False
    
    tags_content = tag_line_match.group(1)
    
    # Check if any tag contains backticks or other YAML-problematic chars
    if '`' not in tags_content and '{' not in tags_content and '}' not in tags_content and '(' not in tags_content and ')' not in tags_content:
        return False
    
    # Split tags by comma (simple approach - works for our case)
    tags = []
    current = ''
    depth = 0
    for c in tags_content:
        if c == '[' or c == '{':
            depth += 1
            current += c
        elif c == ']' or c == '}':
            depth -= 1
            current += c
        elif c == ',' and depth == 0:
            tags.append(current.strip())
            current = ''
        else:
            current += c
    if current.strip():
        tags.append(current.strip())
    
    # Rebuild as block
    new_tags = 'tags:\n'
    for tag in tags:
        stripped = tag.strip()
        # Remove any surrounding quotes
        if (stripped.startswith('"') and stripped.endswith('"')) or \
           (stripped.startswith("'") and stripped.endswith("'")):
            stripped = stripped[1:-1]
        # Always quote if contains special chars
        if any(c in stripped for c in ['`', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '#', ':']):
            escaped = stripped.replace("'", "''")
            new_tags += f"  - '{escaped}'\n"
        else:
            new_tags += f"  - {stripped}\n"
    
    new_frontmatter = re.sub(
        r'^tags:\s*\[.*?\]',
        new_tags.rstrip('\n'),
        frontmatter,
        count=1,
        flags=re.MULTILINE
    )
    
    new_content = content.replace(frontmatter, new_frontmatter)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

# Walk through the wiki directory
wiki_dir = '/tmp/wiki-build/wiki'
fixed_count = 0
for root, dirs, files in os.walk(wiki_dir):
    for f in files:
        if f.endswith('.md'):
            filepath = os.path.join(root, f)
            if fix_tags_in_file(filepath):
                print(f"Fixed: {filepath}")
                fixed_count += 1

print(f"\nFixed {fixed_count} files total")
