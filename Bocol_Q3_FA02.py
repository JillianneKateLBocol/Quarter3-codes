arr = []

#list down their steps for 3 days
steps = {
  "ME": [3500, 5900, 5800],
  "LIEN": [3500, 6740, 4000],
  "KRIS": [4000, 6000, 5700]
}
print(steps)

#Lien's steps for Wednesday
lien = steps["LIEN"][2]
print("Lien's steps for Wednesday:", lien)

#My steps
me = steps["ME"]
print("My steps for Monday:", me)

#update my steps for Monday to 2200
steps["ME"][0] = 2200
print("Updated steps for Monday:", steps["ME"][0])

#My updated steps
steps_updated = steps["ME"]
print("My steps for Monday:", me)
