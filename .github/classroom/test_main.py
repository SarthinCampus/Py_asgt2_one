import subprocess
import sys
import os

def test_output_format():
    script_path = os.path.join("favorite_fruits", "main.py")
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True, check=True)
    output_lines = result.stdout.strip().split("\n")

    assert len(output_lines) == 3, f"Expected 3 lines, got {len(output_lines)}."
    for i, line in enumerate(output_lines):
        assert line.strip(), f"Line {i+1} is empty."
