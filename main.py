"""Two Days of Excuses — make.fun entry.

Writes the locked one-line excuse to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output), no trailing newline.

Verified numbers: 122 chars, 122 bytes, one line.
entry.txt sha256:
2337298b5449805301916cd36ab34e062d80eee8b774b112be5eff6d51431e92
"""

import os

ENTRY = "I finished the report two days early, boss, then spent three days making it perfect. It is perfect. It is also a day late."

# Gate self-check: the entry must be 1-200 chars on a single line.
if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY:
    raise ValueError("entry line violates the 1-200 char one-line gate")

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
