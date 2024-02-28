import json

"""
| problem                                                         | event | category | いいね率 | solves | points |
| --------------------------------------------------------------- | ----- | -------- | -------- | ------ | ------ |
| [Obedient Cat](https://play.picoctf.org/practice/challenge/147) | a     | cate     | 11%      | 101    | 100    |
"""
with open("pico_data.json") as f:
  di = json.load(f)
  # print(di["results"][0])
  print("| problem                                                         | event | category | いいね率 | solves | points | solved |")
  print("| --------------------------------------------------------------- | ----- | -------- | --------: | ------: | ------: | --- |")
  for result in di["results"]:
    row = f"| [{result["name"]}](https://play.picoctf.org/practice/challenge/{result["id"]}) | {result["event"]["name"]} | {result["category"]["name"]} | {int(result["rating_percentage"])}% | {result["users_solved"]} | {result["gym_points"]} | ❌ |"
    print(row)
