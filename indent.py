with open("script.py", "r") as f:
  lines = f.readlines()
for i in range(123, 199):
  lines[i] = "  " + lines[i]
with open("script2.py", "w") as f:
  f.writelines(lines)
