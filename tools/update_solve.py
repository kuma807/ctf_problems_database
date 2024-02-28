solved_problem = input()

def update_problem_readme():
  with open("problem/README.md", mode="r+") as f:
    s = f.read()
    contents = s.split("# 解いた問題")[0][:-2] + "  \n"
    contents += f"[{solved_problem}](#{solved_problem.lower().replace(' ', '-')})  \n\n"
    s = s.replace(s.split("# 解いた問題")[0], contents)
    s += f"\n## {solved_problem}  \n\n## 解き方  \n\n## 学び  \n"
    f.seek(0)
    f.write(s)
    f.truncate()

def update_solved_status():
  with open("README.md", 'r') as file:
    lines = file.readlines()
  
  new_lines = [line.replace("❌", "✅") if (f"[{solved_problem}]" in line) else line for line in lines]
  
  with open("README.md", 'w') as file:
    file.writelines(new_lines)

update_problem_readme()
update_solved_status()
