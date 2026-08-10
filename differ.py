import difflib
import sys
from pathlib import Path

def compare_and_save(file1_path, file2_path, ext=".md"):
    """Compares two files and saves the diff to a new file."""
    try:
        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            file1_lines = f1.readlines()
            file2_lines = f2.readlines()

        # Generate the diff generator (do not cast to list yet)
        diff = difflib.ndiff(file1_lines, file2_lines)

        # Determine output filename (e.g., script_v1_diff.md)
        out_path = Path(file1_path).stem + f"_diff{ext}"

        # Write only the differences with line numbers to the file
        with open(out_path, 'w') as out_file:
            if ext == ".md":
                out_file.write("```diff\n")
            
            line_orig = 1
            line_new = 1
            
            for line in diff:
                marker = line[:2]
                content = line[2:]
                
                if marker == '  ':
                    # Unchanged lines simply advance the counters; nothing is written
                    line_orig += 1
                    line_new += 1
                elif marker == '- ':
                    # Deletions only advance the original file's counter
                    out_file.write(f"Line {line_orig:03d} (Old): - {content}")
                    line_orig += 1
                elif marker == '+ ':
                    # Additions only advance the new file's counter
                    out_file.write(f"Line {line_new:03d} (New): + {content}")
                    line_new += 1
                elif marker == '? ':
                    # Intra-line character highlights do not advance any counter
                    out_file.write(f"                 ? {content}")
            
            if ext == ".md":
                out_file.write("```\n")
                
        print(f"Diff successfully saved to {out_path}")
                
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        compare_and_save(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python diff_script.py <original_file.py> <new_file.py>")