import json

#出力形式
"""
| problem                                                         | event | category | いいね率 | solves | points |
| --------------------------------------------------------------- | ----- | -------- | -------- | ------ | ------ |
| [Obedient Cat](https://play.picoctf.org/practice/challenge/147) | a     | cate     | 11%      | 101    | 100    |
"""

num_participant = {"Beginner picoMini 2022": 5728, "picoCTF 2019": 15817, "picoCTF 2020 Mini-Competition": 3574, "picoCTF 2021": 6215, "picoCTF 2022": 7794, "picoCTF 2023": 6923, "picoMini by redpwn": 248}

print("| problem                                                         | event | category | いいね率 | solves | points | コンテスト中solved率 | solved |")
print("| --------------------------------------------------------------- | ----- | -------- | --------: | ------: | ------: | ---: | --- |")
for i in range(1, 5):
  with open(f"pico_data{i}.json") as f:
    di = json.load(f)
    for result in di["results"]:
      if result["event"] == None:
        result["event"] = {"name": ""}
        result["solved_percent"] = ""
      else:
        result["solved_percent"] = int(result["users_solved_during_event"] / num_participant[result["event"]["name"]] * 1000) / 10
      
      row = f"| [{result["name"]}](https://play.picoctf.org/practice/challenge/{result["id"]}) | {result["event"]["name"]} | {result["category"]["name"]} | {int(result["rating_percentage"])}% | {result["users_solved"]} | {result["gym_points"]} | {result["solved_percent"]} | {"✅" if result["solved_by_user"] else "❌"} |"
      print(row)
