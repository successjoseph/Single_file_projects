# Single_file_projects

![Language](https://img.shields.io/badge/language-mixed-lightgrey)

## About

This repository is a grab-bag of small, standalone, single-file scripts and pages — each one is an independent mini-project with no shared build system, dependencies, or relationship to the others beyond living in the same folder. It is not a cohesive application; it's a personal scratch collection of one-off utilities and practice exercises. Each item is described on its own below.

## Table of Contents

- [About](#about)
- [Contents](#contents)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Contributing](#contributing)
- [Authors and License](#authors-and-license)

## Contents

| File | Type | What it is |
|------|------|------------|
| `auto_SS_taker.py` | Python script | Takes a screenshot every 10 minutes (via `pyautogui`) into a local `shots/` folder, with a live countdown printed to the terminal. Runs until interrupted (Ctrl-C). |
| `differ.py` | Python CLI | Compares two text files line-by-line (`difflib.ndiff`) and writes a readable diff (with old/new line numbers) to a new `<file1>_diff.md` file, wrapped in a fenced code block. |
| `fcctester.py` | Python script | A scratch file of small practice functions (a discount calculator, a simple RPG character-sheet generator) with inline `print()` calls exercising them — reads like FreeCodeCamp-style coding practice rather than a tool meant to be imported/reused. |
| `slc-qr-generator.html` | Static HTML page | A client-side QR code generator built for "Supernatural Life Church" (SLC) — pure HTML/CSS/JS, no build step, loads `qrcodejs` from a CDN with a Subresource Integrity (SRI) hash so a tampered CDN file is blocked by the browser. |
| `success_timetable.html` | Static HTML page | A personal weekly timetable/schedule viewer with a dark, custom-styled UI (Google Fonts, CSS custom properties, a noise-texture background), built for the author's own week planning. |

## Prerequisites

- `auto_SS_taker.py` requires Python 3 and the `pyautogui` package (`pip install pyautogui`).
- `differ.py` and `fcctester.py` require only the Python standard library.
- `slc-qr-generator.html` and `success_timetable.html` are fully self-contained — just open them in a browser (they load fonts/scripts from public CDNs, so an internet connection is needed for those to render as designed).

## Usage

```bash
python auto_SS_taker.py                       # start periodic screenshot capture
python differ.py old_version.py new_version.py  # writes old_version_diff.md
python fcctester.py                            # runs the practice-function print statements
```

For the HTML files, simply open them directly in a browser — no server required.

## Contributing

This is a personal scratch/practice collection, not intended as a coherent open-source project — notes for future you rather than an open contribution target.

## Authors and License

**Author:** [successjoseph](https://github.com/successjoseph)

No license file included — all rights reserved by default.
