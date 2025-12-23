#!/usr/bin/env python3
"""Simple validator to check required XML metadata fields in prompt files."""
import re
from pathlib import Path

REQUIRED = ["<Title>", "<Confidence>", "<Tags>", "<ExampleInput>", "<ExampleOutput>", "<Creator>"]

root = Path(__file__).resolve().parents[1]
files = list(root.glob('role-based-prompts/*.md')) + list(root.glob('Prompt/*.md'))

failures = []
for f in files:
    text = f.read_text(encoding='utf-8')
    missing = [r for r in REQUIRED if r not in text]
    if missing:
        failures.append((f.relative_to(root), missing))

if not failures:
    print('OK: All prompt files contain required metadata.')
else:
    print('FAIL: Missing metadata in some files:')
    for p, missing in failures:
        print(f'- {p}: missing {missing}')
    raise SystemExit(2)
