import datetime
import json

solved_problem = input("問題名")#サイトに表示される問題名
site = input("サイトの名前")
contest = ""
category = ""

# picoCTFの場合はsiteに空行を入力することでコンテスト名、カテゴリの入力を自動で行ってくれるように実装
if site == "":
  site = "picoCTF"
  for i in range(1, 5):
    with open(f"data/pico_data{i}.json") as f:
      di = json.load(f)
      for result in di["results"]:
        if result["name"] == solved_problem:
          if result["event"] != None:
            contest = result["event"]["name"]
          if result["category"] != None:
            category = result["category"]["name"]
else:
  contest = input("コンテスト名")
  category = input("カテゴリー")
utc_now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S')

def update_writeups():
  with open("writeups/README.md", mode="r+") as f:
    s = f.read()
    contents = s.split("# 解いた問題")[0][:-2] + "  \n"
    contents += f"[{solved_problem}](#{solved_problem.lower().replace(' ', '-')})  \n\n"
    s = s.replace(s.split("# 解いた問題")[0], contents)
    s += f"\n# {solved_problem}  \n\nsite: {site}  \ncontest: {contest}  \ncategory: {category}  \n\n## 解き方  \n\n## 学び  \n"
    f.seek(0)
    f.write(s)
    f.truncate()

def update_solved():
  with open("data/solved.json", "r") as file:
    data = json.load(file)
  data["problems"].append({
      "problem": solved_problem,
      "site": site,
      "contest": contest,
      "category": category,
      "time": utc_now
    })
  with open("data/solved.json", "w") as file:
    json.dump(data, file, indent=2)

update_writeups()
update_solved()
