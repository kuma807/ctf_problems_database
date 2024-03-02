import json

#出力形式
"""
| problem                                                         | event | category | いいね率 | solves | points |
| --------------------------------------------------------------- | ----- | -------- | -------- | ------ | ------ |
| [Obedient Cat](https://play.picoctf.org/practice/challenge/147) | a     | cate     | 11%      | 101    | 100    |
"""


print("| problem                                                         | event | category | いいね率 | solves | points | solved |")
print("| --------------------------------------------------------------- | ----- | -------- | --------: | ------: | ------: | --- |")
for i in range(1, 5):
  with open(f"pico_data{i}.json") as f:
    di = json.load(f)
    for result in di["results"]:
      if result["event"] == None:
        result["event"] = {"name": ""}
      row = f"| [{result["name"]}](https://play.picoctf.org/practice/challenge/{result["id"]}) | {result["event"]["name"]} | {result["category"]["name"]} | {int(result["rating_percentage"])}% | {result["users_solved"]} | {result["gym_points"]} | ❌ |"
      print(row)
