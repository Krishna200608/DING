# SETUP for DING

This is a short, written guide to get DING running quickly. No fluff, just the steps that work. (=^ ◡ ^=)

---

## What you need
- Python 3.14.2 (check with `python --version`)
- pip
- Git (to clone the repo)

---

## Get the code
```bash
git clone https://github.com/opencodeiiita/DING.git
cd DING
```

---

## Set up a virtual environment (I will strongly recommended)
```bash
python -m venv venv
```

Activate it:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate` [if you are Unix Fan :) ]

You should see `(venv)` in your terminal prompt.

---

## Install DING
```bash
pip install -e .
```

This installs in editable mode so changes you make in the repo are picked up immediately.

---

## Check the install
```bash

(something appears here)

```
Expected commands: `init`, `hash`, `cat-file`. If you see them, you're set.

---

## Quick start
```bash
mkdir demo
cd demo
ding init                  # create a new DING repo
echo "hello" > note.txt
ding hash note.txt         # store the file and get its hash
ding cat-file <hash_prefix> # print the stored content
```

Replace `<hash_prefix>` with the start of the hash you got from `ding hash`.

---

## If something breaks
- `ding: command not found`: activate the venv, then rerun `pip install -e .`
- `ModuleNotFoundError: No module named 'src'`: run commands from the DING repo root (where `setup.py` lives).
- Wrong Python: use `python3.14 -m venv venv` or install 3.14.2 and try again.
- Install errors: `pip install --upgrade pip setuptools wheel` then `pip install -e .`.

---

## Done
You now have DING installed and a minimal workflow to try it. Keep this close, tweak as you learn, and share fixes back with the team.
ding --help

Enjoy!     
# **ฅ(=✧ω✧=)ฅ**