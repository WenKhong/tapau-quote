# AGENTS.md: tapau-quote
Rules for every coding agent in this repo (Claude Code, Codex, Copilot, Cursor).

## Project
Python CLI: CNY price + shipping → MYR quote (FX rate + margin). One item or a CSV of orders. Uses uv.

## Commands
- Tests: `uv run pytest -q`

## Rules
1. Run the tests and show me the output before saying a task is done.
2. Never edit or delete a test to make it pass. If a test looks wrong, stop and ask.
3. Don't add dependencies without asking first.
4. Made-up data only in tests and samples. No real customer data.