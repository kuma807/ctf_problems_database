import json

#出力形式
"""
| problem                                                         | event | category | いいね率 | solves | points |
| --------------------------------------------------------------- | ----- | -------- | -------- | ------ | ------ |
| [Obedient Cat](https://play.picoctf.org/practice/challenge/147) | a     | cate     | 11%      | 101    | 100    |
"""

num_participant = {"Beginner picoMini 2022": 5728, "picoCTF 2019": 15817, "picoCTF 2020 Mini-Competition": 3574, "picoCTF 2021": 6215, "picoCTF 2022": 7794, "picoCTF 2023": 6923, "picoMini by redpwn": 248}

print("| problem                | event | category | いいね率 | solves | points | solved |")
print("| ----------------------------------- | ----- | -------- | --------: | ------: | ------: | --- |")
for i in range(1, 5):
  with open(f"pico_data{i}.json") as f:
    di = json.load(f)
    for result in di["results"]:
      if result["event"] == None:
        result["event"] = {"name": ""}
        result["solved_percent"] = ""
      else:
        result["solved_percent"] = int(result["users_solved_during_event"] / num_participant[result["event"]["name"]] * 1000) / 10
      
      row = f"| [{result["name"]}](https://play.picoctf.org/practice/challenge/{result["id"]}) | {result["event"]["name"]} | {result["category"]["name"]} | {int(result["positive_rating_count"] / result["rating_count"])}% | {result["users_solved"]} | {result["gym_points"]} | {"✅" if result["solved_by_user"] else "❌"} |"
      print(row)

with open("../data/solved.json", "r") as file:
    data = json.load(file)
for i in range(1, 5):
    with open(f"pico_data{i}.json") as f:
      di = json.load(f)
      for result in di["results"]:
        problem = result["name"]
        site = "picoCTF"
        contest = ""
        category = ""
        if result["event"] != None:
          contest = result["event"]["name"]
        if result["category"] != None:
          category = result["category"]["name"]
        data["problems"].append({
            "problem": problem,
            "site": site,
            "contest": contest,
            "category": category,
        })
with open("../data/solved.json", "w") as file:
    json.dump(data, file, indent=4)
