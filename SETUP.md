# SETUP Guide for DING

_Get up and running with DING in under 5 minutes!_

---

## Prerequisites

Before starting, make sure you have:

- **Python 3.14.2** installed on your system
  - Check with: `python --version` or `python3 --version`
  - Using a Python version manager like `pyenv` is recommended
- **pip** (Python package manager) - usually comes with Python
- **Git** (for cloning the repository)

---

## Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/opencodeiiita/DING.git
cd DING
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

> **Why virtual environment?** It keeps DING's dependencies isolated from your system Python.

### Step 3: Install DING

```bash
pip install -e .
```

> The `-e` flag installs DING in **editable mode**, so changes to the code are reflected immediately.

---

## Verify Installation

Test if DING is installed correctly:

```bash
ding --help
```

You should see a list of available commands:
- `init` — Initialize an empty DING repository
- `hash` — Hash and store a file
- `cat-file` — Decompress and print file data

---

## Quick Start

### Initialize a New Repository

```bash
# Create a test directory
mkdir my-ding-repo
cd my-ding-repo

# Initialize DING
ding init
```

This creates a `.ding/` directory with internal metadata and object storage, similar to Git's `.git/`.

### Hash and Store a File

```bash
# Create a test file
echo "Hello, DING!" > test.txt

# Hash and store it
ding hash test.txt
```

### Retrieve File Data

```bash
# Get the hash from the previous command, then:
ding cat-file <hash>
```

---

## Troubleshooting

**Issue:** `ding` command not found
- **Solution:** Make sure the virtual environment is activated (if using one), or reinstall with `pip install -e .`

**Issue:** `ModuleNotFoundError: No module named 'src'`
- **Solution:** Run from the DING repository root directory

**Issue:** Python version error
- **Solution:** Make sure you have Python 3.7 or higher. Check with `python --version`

---

## Next Steps

- Read the [README.md](README.md) for a detailed overview of DING's features
- Check the [CONTRIBUTING.md](CONTRIBUTING.md) to start contributing
- Explore the `src/` directory to understand the codebase

---

**Happy coding!** 🚀
