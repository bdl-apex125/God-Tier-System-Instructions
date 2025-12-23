# Contributing to God-Tier System Instructions

Thank you for wanting to contribute. Please follow these rules so contributions remain high-quality and machine-friendly.

## What to provide
- Use XML-style tags for prompt metadata. Example header:

  <Prompt>
    <Title>Example Prompt</Title>
    <Confidence>0.95</Confidence>
    <Tags>persona,code,analysis</Tags>
  </Prompt>

- Provide a clear `Confidence` score between 0.0 and 1.0 indicating how reliable the prompt/contents are.
- Include at least one real-world example (input → expected output) demonstrating the prompt's intended behavior.

## File placement
- Add persona or task-specific prompts under `role-based-prompts/` as Markdown files.
- Core frameworks (CO-STAR, Chain-of-Thought guides) belong in `core-frameworks/`.
- XML templates go in `xml-templates/`.

## Pull request checklist
- [ ] I added XML metadata at top of my prompt file.
- [ ] I included a confidence score and at least one example.
- [ ] I added the file to the correct folder.

## Review process
Maintainers will review for clarity, accuracy, and adherence to XML metadata conventions. Expect feedback if examples or metadata are missing.
