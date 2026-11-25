import os

line = "We ride together every morning and I still don't know your model number. I think about that a lot."

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)

# Verify the write landed intact.
with open("/output/entry.txt", encoding="utf-8") as f:
    assert f.read() == line

# Second opinion on the file, this time in raw bytes: the gate wants
# 1 to 200 characters, so check the exact byte count as well as the text.
with open("/output/entry.txt", "rb") as f:
    raw = f.read()
assert len(raw) == 98 and raw == line.encode("utf-8")
assert 1 <= len(line) <= 200
