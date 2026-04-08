import os
import emoji

# ==========================================
# CONFIGURATION - LIST OF FILES TO PROCESS
# ==========================================
FILES_TO_PROCESS = [
    "file.py",
]

POLISH_CHARS_STR = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"

# Translation table for Polish characters to ASCII equivalents
POLISH_CHARS_MAP = str.maketrans({
    'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
    'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N', 'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
})
# ==========================================

def count_polish_chars(text):
    """Counts occurrences of Polish characters in a given string."""
    return sum(1 for char in text if char in POLISH_CHARS_STR)

def process_and_clean_file(input_file, remove_emojis_flag, replace_polish_flag):
    base_name, extension = os.path.splitext(input_file)
    output_file = f"{base_name}_cleaned{extension}"

    try:
        with open(input_file, 'r', encoding='utf-8') as f_in:
            original_content = f_in.read()
            
        current_content = original_content
        
        # Stats containers
        input_emoji_count = 0
        output_emoji_count = 0
        unique_emojis_str = "None"
        
        input_pl_count = 0
        output_pl_count = 0

        # 1. Handle Emoji statistics and removal
        if remove_emojis_flag:
            found_emojis_data = emoji.emoji_list(current_content)
            input_emoji_count = len(found_emojis_data)
            unique_emojis_str = "".join(list(set(item['emoji'] for item in found_emojis_data))) or "None"
            current_content = emoji.replace_emoji(current_content, replace='')
            output_emoji_count = len(emoji.emoji_list(current_content))

        # 2. Handle Polish character statistics and translation
        if replace_polish_flag:
            input_pl_count = count_polish_chars(current_content)
            current_content = current_content.translate(POLISH_CHARS_MAP)
            output_pl_count = count_polish_chars(current_content)

        # CHECK: If content is identical, no changes were needed
        if original_content == current_content:
            print(f"--- Skipping: '{input_file}' ---")
            print("Reason: No targeted characters found to clean.")
            print("-" * 45)
            return

        # Write the cleaned file
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write(current_content)

        # REPORT GENERATION
        print(f"--- Processed: '{input_file}' ---")
        
        if remove_emojis_flag:
            print(f"[EMOJI STATS]")
            print(f"  - Unique found: {unique_emojis_str}")
            print(f"  - Count (In):  {input_emoji_count}")
            print(f"  - Count (Out): {output_emoji_count}")
            
        if replace_polish_flag:
            print(f"[POLISH CHAR STATS]")
            print(f"  - Count (In):  {input_pl_count}")
            print(f"  - Count (Out): {output_pl_count}")
            
        print(f"Saved as: '{output_file}'")
        print("-" * 45)

    except FileNotFoundError:
        print(f"[ERROR] File '{input_file}' not found.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")

def main():
    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=========================================")
    print("       ADVANCED FILE CLEANUP TOOL        ")
    print("=========================================")
    print("1. Remove Emojis")
    print("2. Replace Polish Characters")
    print("3. Both (Emojis & Polish Characters)")
    print("=========================================")
    
    choice = input("Select mode (1/2/3): ").strip()
    
    rem_emoji = choice in ['1', '3']
    rep_polish = choice in ['2', '3']
    
    if choice not in ['1', '2', '3']:
        print("Invalid selection. Operation cancelled.")
        return

    print("\nStarting process...\n")
    for file in FILES_TO_PROCESS:
        process_and_clean_file(file, rem_emoji, rep_polish)
    print("Finished.")

if __name__ == "__main__":
    main()
