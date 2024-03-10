import json

site = "picoCTF"

ls = []
dic = {}
for i in range(1, 5):
  with open(f"pico_data{i}.json") as f:
    di = json.load(f)
    for result in di["results"]:
      ls.append(f"# {result["name"]}")
      problem = result["name"]
      site = "picoCTF"
      contest = ""
      category = ""
      if result["event"] != None:
        contest = result["event"]["name"]
      if result["category"] != None:
        category = result["category"]["name"]
      dic[problem] = {
        "site": site,
        "contest": contest,
        "category": category,
      }
    
with open("../problem/README.md", 'r') as file:
  lines = file.readlines()
  new_lines = []
  problem = ""
  for line in lines:
    found = False
    for a in ls:
      if a in line:
        found = True
        problem = a[2:]
    if found:
      line += f"\nsite: {dic[problem]["site"]}  \ncontest: {dic[problem]["contest"]}  \ncategory: {dic[problem]["category"]}\n"
    new_lines.append(line)
  
  with open("../problem/README.md", 'w') as file:
    file.writelines(new_lines)
