# PyTextSanitizer 🧹

A powerful, interactive Python utility designed to clean up your codebase or text files. It completely strips out emojis and normalizes Polish characters into standard ASCII equivalents, keeping your files clean and universally readable.

## 🚀 Features

*   **Interactive Menu:** Choose exactly what you want to clean (Emojis only, Polish characters only, or both) right from the terminal.
*   **Flawless Emoji Removal:** Powered by the official `emoji` library, it catches everything—including the newest Unicode additions, skin-tone modifiers, and Zero Width Joiners (ZWJ) that regular expressions often miss.
*   **ASCII Normalization:** Seamlessly translates Polish diacritics (`ą`, `ć`, `ę`, `ł`, `ń`, `ó`, `ś`, `ź`, `ż`) to their standard ASCII counterparts (`a`, `c`, `e`, `l`, `n`, `o`, `s`, `z`, `z`).
*   **Smart Skipping:** If a file doesn't contain any targeted characters, the script skips it entirely to avoid creating unnecessary duplicates.
*   **Detailed Reports:** Generates a precise console summary for each processed file, including the exact count of characters modified and unique emojis found.

## 🛠️ Prerequisites

The script requires Python 3.x and the `emoji` package to run. Install the required dependency using pip:

```bash
pip install emoji
```

## 💻 Usage

1.  Clone or download this repository.
2.  Open the Python script (e.g., `cleaner.py`) in your text editor.
3.  Locate the `FILES_TO_PROCESS` list at the top of the file and add the paths to the files you want to clean:

    ```python
    FILES_TO_PROCESS = [
        "file1.py",
        "data/config.json",
        "readme_draft.txt"
    ]
    ```

4.  Run the script from your terminal:

    ```bash
    python cleaner.py
    ```

5.  Select your desired cleaning mode from the interactive menu.

## 📂 Output

The script reads your original files and creates new, sanitized copies in the same directory, appending `_cleaned` to the original filename. (e.g., `your_script.py` becomes `your_script_cleaned.py`). Your original files remain completely untouched and safe.

## 📊 Example Console Output

```plaintext
=========================================
       ADVANCED FILE CLEANUP TOOL        
=========================================
1. Remove Emojis
2. Replace Polish Characters
3. Both (Emojis & Polish Characters)
=========================================
Select mode (1/2/3): 3
Starting process...
--- Processed: 'file1.py' ---
[EMOJI STATS]
  - Unique found: 🚀🔥⏹️
  - Count (In):  5
  - Count (Out): 0
[POLISH CHAR STATS]
  - Count (In):  12
  - Count (Out): 0
Saved as: 'brainrot_cleaned.py'
---------------------------------------------
--- Skipping: 'dictionary.py' ---
Reason: No targeted characters found to clean.
---------------------------------------------
Finished.
```

## 📝 License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as you see fit.
