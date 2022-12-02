from pathlib import Path

s = Path("./d1_input.txt").read_text()

elfs = [sum(map(int, elf.split("\n"))) for elf in s.split("\n\n")]
print("max", max(elfs))
print("top3", sum(sorted(elfs)[-3:]))
