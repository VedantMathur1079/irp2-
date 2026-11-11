"""Run every problem against its test cases in tests/ and report pass/fail."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
failed = 0

for case_dir in sorted((ROOT / "tests").iterdir()):
    script = ROOT / "problems" / (case_dir.name + ".py")
    for inp in sorted(case_dir.glob("input_*.txt")):
        exp = case_dir / inp.name.replace("input_", "expected_")
        result = subprocess.run([sys.executable, str(script)], input=inp.read_text(),
                                capture_output=True, text=True)
        ok = result.stdout.strip() == exp.read_text().strip()
        failed += not ok
        print(("PASS" if ok else "FAIL"), case_dir.name, inp.name)

print("\nAll tests passed." if failed == 0 else f"\n{failed} test(s) failed.")
sys.exit(1 if failed else 0)
