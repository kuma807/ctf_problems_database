import json

data = {"problems": []}

for i in range(1, 5):
    with open(f"data/pico_data{i}.json") as f:
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
        if result["solved_by_user"]:
          data["problems"].append({
              "problem": problem,
              "site": site,
              "contest": contest,
              "category": category,
          })
          
with open("data/solved.json", "w") as file:
    json.dump(data, file, indent=2)
