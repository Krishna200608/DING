# SETUP Guide for DING 🚀

_A Version Control System that slaps. Get it running in under 5 minutes. No cap._

---

## 📋 TL;DR (The Speedrun)

```bash
git clone https://github.com/opencodeiiita/DING.git
cd DING
python -m venv venv
# On Windows: venv\Scripts\activate | On Mac/Linux: source venv/bin/activate
pip install -e .
ding --help  # profit
```

Done. You're cooked up. 💯

---

## Prerequisites (The Boring Part)

Make sure you got:

- **Python 3.14.2** (yeah, we're fancy)
  - Check: `python --version`
  - Get it from [python.org](https://www.python.org) or use `pyenv` if you're a real one
- **pip** (comes with Python, no cap)
- **Git** (for cloning, duh)

> **Pro Tip:** If you have multiple Python versions installed, use `python3.14` explicitly to avoid version drama.

---

## 🔧 Installation (The Cook)

### Step 1: Clone the Repo

```bash
git clone https://github.com/opencodeiiita/DING.git
cd DING
```

### Step 2: Set Up Virtual Environment

**Why?** Keeps DING isolated. Imagine if all your Python projects fought each other—chaos. Don't be that person.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Your terminal should now show `(venv)` at the start. If it doesn't, you cooked it. Try again.

### Step 3: Install DING

```bash
pip install -e .
```

The `-e` flag = editable mode. Changes go brrr instantly. No reinstalling needed. Modern problems require modern solutions.

---

## ✅ Verify It Works

```bash
ding --help
```

You should see:
```
usage: ding [-h] {init,hash,cat-file} ...

positional arguments:
  {init,hash,cat-file}
    init              initializes an empty ding repository
    hash              hashes and stores the file
    cat-file          prints out the uncompressed data
```

If you see this, you're in. If not, check the Troubleshooting section (it has answers, fr).

---

## 🎮 Quick Start (The Fun Part)

### Initialize Your First DING Repo

```bash
mkdir my-project
cd my-project
ding init
```

Boom. You just created a `.ding/` folder. That's DING's internal folder, like Git's `.git/` but make it make sense.

### Hash a File (Content-Addressable Storage Goes Brrrr)

```bash
echo "DING is actually fire" > test.txt
ding hash test.txt
```

Output:
```
abc123def456...
```

That's the hash. DING compressed and stored your file. It's like zip but cooler because it's content-addressable.

### Get Your File Back (Decompress)

```bash
ding cat-file abc123
```

See your file content again. Magic. ✨

---

## 🧠 Deeper Understanding (Optional Read)

### What Just Happened?

1. **`ding init`** creates a `.ding/` directory with:
   - `objects/` — stores your compressed blobs, trees, and commits
   - Metadata files for the DING system

2. **`ding hash`** takes a file and:
   - Reads it
   - Compresses it
   - Creates a SHA-1 hash (like Git does, but our own implementation)
   - Stores it in `objects/`

3. **`ding cat-file`** retrieves and decompresses data by its hash

This is the foundation of Version Control™.

---

## 🚨 Troubleshooting (Solutions Are Here, Trust)

### `ding: command not found`
**Problem:** DING isn't in your PATH or venv isn't activated.

**Fix:**
```bash
# Check if venv is activated (you should see (venv) in your terminal)
# If not:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Then reinstall:
pip install -e .
```

### `ModuleNotFoundError: No module named 'src'`
**Problem:** You're running commands from the wrong directory.

**Fix:**
```bash
cd /path/to/DING  # Go to the repo root where setup.py is
ding --help
```

### `Python version mismatch`
**Problem:** You don't have Python 3.14.2 or it's not the default.

**Fix:**
```bash
python3.14 --version  # Check if it exists
python3.14 -m venv venv  # Use it explicitly
```

Or install pyenv:
```bash
# macOS/Linux
brew install pyenv
pyenv install 3.14.2
pyenv local 3.14.2

# Windows (use pyenv-win)
# Then: pyenv local 3.14.2
```

### `pip install -e . fails`
**Problem:** Dependencies or permissions issue.

**Fix:**
```bash
pip install --upgrade pip setuptools wheel
pip install -e .
```

If still broken: `pip install -e . -v` (verbose mode shows what's happening)

---

## 📚 Project Structure (Quick Ref)

```
DING/
├── setup.py           # Installation config
├── README.md          # What is DING?
├── SETUP.md           # This file (you're reading it!)
├── CONTRIBUTING.md    # How to contribute
└── src/
    ├── cli.py         # Command-line interface
    ├── data.py        # Core logic (hashing, compression)
    ├── base.py        # Base classes (empty for now, potential expansion)
    └── __pycache__/   # Compiled Python (ignore this)
```

---

## 🎯 Next Steps

- [ ] Read [README.md](README.md) — understand the full vision
- [ ] Check [CONTRIBUTING.md](CONTRIBUTING.md) — want to contribute? Start here
- [ ] Explore `src/data.py` — see how the magic happens
- [ ] Create your first DING repo — experiment!
- [ ] Break things and fix them — learning speedrun any%

---

## 💡 Pro Tips (Sigma Grindset Edition)

1. **Use `ding hash` on multiple files to understand the system**
   ```bash
   ding hash file1.txt
   ding hash file2.txt
   # Different files = different hashes. It's that simple.
   ```

2. **Check what's inside `.ding/objects/`**
   ```bash
   ls .ding/objects/  # (or dir on Windows)
   # You'll see your compressed files stored there
   ```

3. **Try hashing the same file twice**
   ```bash
   ding hash test.txt  # Hash: abc123
   ding hash test.txt  # Hash: abc123 (same! Content-addressable!)
   ```

4. **Modify a file and hash it again**
   ```bash
   echo "new content" > test.txt
   ding hash test.txt  # Different hash now
   ```

This is how Git works under the hood. DING is your front-row seat to the magic.

---

## ❓ FAQ (The Speedrun Questions)

**Q: Do I need to use a virtual environment?**  
A: Nah, but do you want to explain to your 5-year-old why your entire Python setup is broken? Venv = sanity.

**Q: Can I use Python 3.13 or 3.12?**  
A: Probably, but we're standardizing on 3.14.2. Just use that, bro.

**Q: What if I already have DING installed but want to update?**  
A: `pip install --upgrade -e .` (in the repo directory)

**Q: Is DING production-ready?**  
A: No, it's educational. But the concepts are real and Git-adjacent.

**Q: Can I use DING instead of Git?**  
A: lol no, but you'll understand Git way better after this.

---

## 🤝 Getting Help

- **Confused?** Check this guide again (you probably missed something in the TL;DR section)
- **Found a bug?** Open an issue on GitHub
- **Stuck?** Ask on Discord or check the [CONTRIBUTING.md](CONTRIBUTING.md)
- **Need updates?** Star the repo and check back (future maintainers will cook harder docs)

---

## 🎉 You Made It

Congrats, you've successfully set up DING. You're now part of an exclusive club of people who understand version control systems. That's actually fire.

Now go forth and hash some files. 🔥

---

_Last Updated: January 2026 | Maintained by OpenCode IIITA_
