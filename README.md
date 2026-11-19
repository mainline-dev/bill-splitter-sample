# Bill splitter sample

A small Python project for trying [Mainline](https://mainline.dev) with a coding agent.

Mainline keeps a team's stories on a story map, each with the scenarios that say when it is done. A coding agent connected to Mainline reads a story and its scenarios, then builds it one scenario at a time, with a failing test first. This project gives the agent something to build.

## What is here

It splits a restaurant bill between the people at the table. Amounts are in pence, so nothing is lost to rounding.

- `bill_splitter.py` has one function, `split_evenly`.
- `tests/` has its tests.

The project goes with a Mainline map called **Bill Splitter**, which has four stories:

| Story | State |
|---|---|
| A diner splits a bill evenly | released: the code in this repository |
| A diner adds a tip before splitting | active, with two scenarios: the next one to build |
| A diner leaves someone out of a shared item | planned, with two scenarios |
| A diner splits by what each person ordered | planned, with no scenarios yet |

## Clone, install and run the tests

You need Python 3.9 or later.

```sh
git clone https://github.com/mainline-dev/bill-splitter-sample.git
cd bill-splitter-sample
python3 -m venv .venv
. .venv/bin/activate
pip install pytest
pytest
```

Three tests pass.

## Connect a coding agent to Mainline

You need a Mainline account on a team that has the Bill Splitter map.

### Claude Code

Install the Mainline plugin, then add the Mainline server:

```sh
claude plugin marketplace add mainline-dev/plugins
claude plugin install mainline@mainline-dev
claude mcp add --transport http mainline https://mainline.dev/mcp
```

Start Claude Code in this folder, type `/mcp`, choose `mainline` and authenticate. Your browser opens Mainline. Sign in, tick the team with the Bill Splitter map and approve.

### Codex

```sh
codex plugin marketplace add mainline-dev/plugins
codex plugin add mainline@mainline-dev
codex mcp add mainline --url https://mainline.dev/mcp
```

Your browser opens Mainline. Sign in, tick the team with the Bill Splitter map and approve. Start a new Codex session in this folder.

## Work the next story

Ask the agent:

```
Work the next story on the Bill Splitter map.
```

What it should do:

1. Read the map and ask which story to work on. Choose "A diner adds a tip before splitting". It is the active one, assigned to you.
2. Read that story's two scenarios.
3. Take the first scenario, write a test for it in `tests/` and run it to see it fail.
4. Write the smallest change to `bill_splitter.py` that passes it, run all the tests and commit, with the story's short ID in the message.
5. Do the same for the second scenario.
6. Stop and prepare a walkthrough of the change. It marks nothing done in Mainline: the agent can read Mainline and cannot change it.

Then ask it for a story that is not ready:

```
Work the story "A diner splits by what each person ordered".
```

That story has no scenarios, so nothing says what done means. The agent should stop and ask for scenarios, and write no code.

## Licence

MIT. See [LICENSE](LICENSE).
