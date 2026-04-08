# PyTextSanitizer 🧹

A powerful, interactive Python utility designed to clean up your codebase or text files. It completely strips out emojis and normalizes Polish characters into standard ASCII equivalents, keeping your files clean and universally readable.

## 🚀 Features

* **Interactive Menu:** Choose exactly what you want to clean (Emojis only, Polish characters only, or both) right from the terminal.
* **Flawless Emoji Removal:** Powered by the official `emoji` library, it catches everything—including the newest Unicode additions, skin-tone modifiers, and Zero Width Joiners (ZWJ) that regular expressions often miss.
* **ASCII Normalization:** Seamlessly translates Polish diacritics (ą, ć, ę, ł, ń, ó, ś, ź, ż) to their standard ASCII counterparts (a, c, e, l, n, o, s, z, z).
* **Smart Skipping:** If a file doesn't contain any targeted characters, the script skips it entirely to avoid creating unnecessary duplicates.
* **Detailed Reports:** Generates a precise console summary for each processed file, including the exact count of characters modified and unique emojis found.

## 🛠️ Prerequisites

The script requires Python 3.x and the `emoji` package to run. 

Install the required dependency using pip:
```bash
pip install emoji
