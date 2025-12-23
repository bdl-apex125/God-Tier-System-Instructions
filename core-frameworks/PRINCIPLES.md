# Core Principles for BDL Apex Prime v3.0

This document lists the authoritative principles all prompts, sets, and integrations in this repository must follow.

1. CO-STAR Compliance
   - Every prompt or set must clearly declare Context, Objective, Style, Tone, Audience, and Response when applicable.
   - The `Response` field must specify an exact output format (Markdown, JSON, Code block, etc.).

2. Zero-Latency First
   - Prompts should avoid conversational padding; primary results or headers must appear first.

3. Precision Reasoning (Structured CoT)
   - For analytical or code tasks, provide a verifiable chain-of-thought or reasoning steps (structured, concise).

4. Hallucination Control / Insufficient Data
   - If facts cannot be verified, the prompt/agent must return `Insufficient Data` or an explicit failure mode rather than fabricating.

5. Metadata & Machine-Friendliness
   - All prompt files must include XML metadata: `<Prompt>` with at least `<Title>`, `<Confidence>`, `<Tags>`, and one example (`<ExampleInput>`, `<ExampleOutput>`).

6. Attribution & Licensing
   - Prompts derived from external sources must include a `<Creator>` tag or reference to `CREDITS.md`.

7. Test Examples
   - Each prompt must include at least one real example (input → expected output) that can be used for validation.

How sets must comply
- Each `sets/SET_*.md` file must include an `<AdheresTo>` reference pointing to this file.
- Sets must list included files and show which principle(s) they enforce.

Enforcement checklist (for maintainers)
- [ ] CO-STAR fields present where required
- [ ] XML metadata present in each prompt file
- [ ] Example input/output included
- [ ] Creator/credits present if derived
