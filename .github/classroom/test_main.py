import subprocess
import sys

def test_output_format():
    # Run the student's script
    result = subprocess.run([sys.executable, "favorite_fruits/main.py"], capture_output=True, text=True, check=True)
    output_lines = result.stdout.strip().split("\n")

    # Check there are exactly 3 lines
    assert len(output_lines) == 3, f"Expected 3 lines, but got {len(output_lines)}. Make sure you're printing exactly 3 fruits."

    # Check that each line is not empty
    for i, line in enumerate(output_lines):
        assert line.strip(), f"Line {i+1} is empty. Each line should contain a fruit name."
