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
    result = []
    i = 0
    n = len(content)

    while i < n:
        if i < n - 1 and content[i:i+2] == '$$':
            end = content.find('$$', i + 2)
            if end != -1:
                result.append(content[i:end+2])
                i = end + 2
                continue

        if content[i] == '$':
            end = content.find('$', i + 1)
            if end != -1 and '\n' not in content[i+1:end]:
                result.append(content[i:end+1])
                i = end + 1
                continue

        if content[i] == '\\' and i + 1 < n:
            next_char = content[i+1]
            if next_char in '#*[]().!|-+`~&_':
                result.append(next_char)
                i += 2
                continue
            elif next_char == '\\':
                result.append('\\\\')
                i += 2
                continue
            else:
                result.append('\\')
                i += 1
                continue

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
    with open(stub_path) as f:
        content = f.read()
    placeholder_match = re.search(r'\{/\* Content from .+? \*/\}', content)
    if placeholder_match:
        header = content[:placeholder_match.start()]
        header = header.rstrip() + '\n\n'
        return header
    return content + '\n\n'


def write_mdx(stub_filename, raw_content):
    stub_path = os.path.join(STUB_DIR, stub_filename)
    header = get_stub_header(stub_path)
    processed = unescape_markdown_and_escape_braces(raw_content)
    final_content = header + processed + '\n'
    with open(stub_path, 'w') as f:
        f.write(final_content)
    print(f'Written: {stub_filename}')


def load_from_disk(tool_result_filename):
    path = os.path.join(TOOL_RESULTS_DIR, tool_result_filename)
    with open(path) as f:
        data = json.load(f)
    return data['fileContent']


write_mdx('qft_5_feynman_diagrams_and_tree_level_qed.mdx',
          load_from_disk('toolu_01MKmYdDQjkEr3DYX34pTxtF.txt'))
write_mdx('qft_6_loop_diagrams_and_regularization.mdx',
          load_from_disk('toolu_018Jid5jFsXzcs4ct2GUnrWD.txt'))
write_mdx('qft_12_standard_model.mdx',
          load_from_disk('toolu_01UfmnbP7EhEEAvkDNZBYhdx.txt'))
write_mdx('qft_13_finite_temperature.mdx',
          load_from_disk('toolu_01UY8y6H7s7cCDnxGvdkBEQe.txt'))
write_mdx('qft_17_anomalies_in_depth.mdx',
          load_from_disk('toolu_01VmDfYf1aQLxWSwQV97mvn8.txt'))
write_mdx('qft_20_supersymmetry_foundations.mdx',
          load_from_disk('toolu_0192U7viMw6JQWa9C6QxKST3.txt'))
write_mdx('qft_26_approaches_to_quantum_gravity.mdx',
          load_from_disk('toolu_01UaK8UKRqfPkxRbnu5UG77A.txt'))

print("Done.")
