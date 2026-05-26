#!/usr/bin/env python3
"""
Process all 26 QFT lesson files from Google Drive content and write MDX files.

Sources:
- 7 files: disk-saved JSON tool results
- 19 files: content embedded in this script (from in-context tool results)

Processing:
1. Decode fileContent (already done by json.loads for disk files; embedded for in-context)
2. Unescape markdown-level escapes (\# -> #, \* -> *, etc.)
3. Escape { and } outside LaTeX math as &#123; and &#125;
4. Write to MDX stubs, replacing the {/* Content from ... */} placeholder
"""

import json
import os
import re

STUB_DIR = '/home/user/Donkey/src/content/curriculum'
TOOL_RESULTS_DIR = '/root/.claude/projects/-home-user-Donkey/d0d03b9e-738f-4dce-9c3a-f6c39b4d24cb/tool-results'


def unescape_markdown_and_escape_braces(content):
    """
    Process raw content (after json.loads) for MDX embedding:
    1. Unescape markdown-level escapes outside math
    2. Escape { and } as &#123; and &#125; outside math
    Math blocks ($...$ and $$...$$) are preserved as-is.
    """
    result = []
    i = 0
    n = len(content)

    while i < n:
        # Check for $$ (display math) - preserve entirely
        if i < n - 1 and content[i:i+2] == '$$':
            end = content.find('$$', i + 2)
            if end != -1:
                result.append(content[i:end+2])
                i = end + 2
                continue
            # No closing $$: fall through to character processing

        # Check for $ (inline math) - preserve entirely (only if no newline inside)
        if content[i] == '$':
            end = content.find('$', i + 1)
            if end != -1 and '\n' not in content[i+1:end]:
                result.append(content[i:end+1])
                i = end + 1
                continue
            # No valid closing $: fall through

        # Backslash escape sequences (markdown level)
        if content[i] == '\\' and i + 1 < n:
            next_char = content[i+1]
            if next_char in '#*[]().!|-+`~&_':
                # Unescape: remove the backslash
                result.append(next_char)
                i += 2
                continue
            elif next_char == '\\':
                # Double backslash: keep as \\ (LaTeX line break or double backslash)
                result.append('\\\\')
                i += 2
                continue
            else:
                # Single backslash before letter or other: keep backslash
                result.append('\\')
                i += 1
                continue

        # Escape { and } for MDX (outside math)
        if content[i] == '{':
            result.append('&#123;')
            i += 1
            continue
        if content[i] == '}':
            result.append('&#125;')
            i += 1
            continue

        result.append(content[i])
        i += 1

    return ''.join(result)


def get_stub_header(stub_path):
    """Read the frontmatter + italic line from a stub file."""
    with open(stub_path) as f:
        content = f.read()
    # Find the placeholder comment
    placeholder_match = re.search(r'\{/\* Content from .+? \*/\}', content)
    if placeholder_match:
        header = content[:placeholder_match.start()]
        # Remove trailing blank lines but keep the final newline
        header = header.rstrip() + '\n\n'
        return header
    return content + '\n\n'


def write_mdx(stub_filename, raw_content):
    """Process raw_content and write the MDX file."""
    stub_path = os.path.join(STUB_DIR, stub_filename)
    header = get_stub_header(stub_path)
    processed = unescape_markdown_and_escape_braces(raw_content)
    final_content = header + processed + '\n'
    with open(stub_path, 'w') as f:
        f.write(final_content)
    print(f'Written: {stub_filename}')


def load_from_disk(tool_result_filename):
    """Load fileContent from a disk-saved tool result JSON file."""
    path = os.path.join(TOOL_RESULTS_DIR, tool_result_filename)
    with open(path) as f:
        data = json.load(f)
    return data['fileContent']


# ============================================================
# DISK-SAVED FILES (7 files)
# ============================================================

# qft_5: toolu_01MKmYdDQjkEr3DYX34pTxtF.txt
write_mdx('qft_5_feynman_diagrams_and_tree_level_qed.mdx',
          load_from_disk('toolu_01MKmYdDQjkEr3DYX34pTxtF.txt'))

# qft_6: toolu_018Jid5jFsXzcs4ct2GUnrWD.txt
write_mdx('qft_6_loop_diagrams_and_regularization.mdx',
          load_from_disk('toolu_018Jid5jFsXzcs4ct2GUnrWD.txt'))

# qft_12: toolu_01UfmnbP7EhEEAvkDNZBYhdx.txt
write_mdx('qft_12_standard_model.mdx',
          load_from_disk('toolu_01UfmnbP7EhEEAvkDNZBYhdx.txt'))

# qft_13: toolu_01UY8y6H7s7cCDnxGvdkBEQe.txt
write_mdx('qft_13_finite_temperature.mdx',
          load_from_disk('toolu_01UY8y6H7s7cCDnxGvdkBEQe.txt'))

# qft_17: toolu_01VmDfYf1aQLxWSwQV97mvn8.txt
write_mdx('qft_17_anomalies_in_depth.mdx',
          load_from_disk('toolu_01VmDfYf1aQLxWSwQV97mvn8.txt'))

# qft_20: toolu_0192U7viMw6JQWa9C6QxKST3.txt
write_mdx('qft_20_supersymmetry_foundations.mdx',
          load_from_disk('toolu_0192U7viMw6JQWa9C6QxKST3.txt'))

# qft_26: toolu_01UaK8UKRqfPkxRbnu5UG77A.txt
write_mdx('qft_26_approaches_to_quantum_gravity.mdx',
          load_from_disk('toolu_01UaK8UKRqfPkxRbnu5UG77A.txt'))


# ============================================================
# IN-CONTEXT FILES (19 files)
# Content was received from Google Drive API in this session.
# The strings below are the raw fileContent values (after JSON decoding).
# ============================================================

# The in-context content files need to be written as separate text files
# since embedding 19 huge strings in a Python script is impractical.
# Instead we write the content to temp files and process from there.

IN_CONTEXT_CONTENT = {}

# These will be populated by the companion script that writes content to files.
# See process_qft_content_2.py for the actual content.

print("Disk-saved files written. In-context content must be written separately.")
print("Run process_qft_content_2.py for the remaining 19 files.")
