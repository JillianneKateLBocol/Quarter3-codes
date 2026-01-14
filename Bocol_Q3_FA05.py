arr = []

#list down their steps for 3 days
steps = {
  "ME": [3500, 5900, 5800],
  "LIEN": [3500, 6740, 4000],
  "KRIS": [4000, 6000, 5700]
}
print(steps)

#Lien's steps for Monday
lien = steps["LIEN"][0]
print("Lien's steps for Monday:", lien)
#Lien's steps for Tuesday
lien = steps["LIEN"][1]
print("Lien's steps for Tuesday:", lien)
#Lien's steps for Wednesday
lien = steps["LIEN"][2]
print("Lien's steps for Wednesday:", lien)

#My steps
me = steps["ME"][0]
print("My steps for Monday:", me)
#My steps
me = steps["ME"][1]
print("My steps for Tuesday:", me)
#My steps
me = steps["ME"][2]
print("My steps for Wednesday:", me)

#kris steps in monday
kris = steps["KRIS"][0]
print("Kris steps for Monday:", kris)
#kris steps in tuesday
kris = steps["KRIS"][1]
print("Kris steps for Tuesday:", kris)
#kris steps in wednesday
kris = steps["KRIS"][2]
print("Kris steps for Wednesday:", kris)

#identify the most active day OVERALL
total_monday = steps["ME"][0] + steps["LIEN"][0] + steps["KRIS"][0]
total_tuesday = steps["ME"][1] + steps["LIEN"][1] + steps["KRIS"][1]
total_wednesday = steps["ME"][2] + steps["LIEN"][2] + steps["KRIS"][2]

if total_monday > total_tuesday and total_monday > total_wednesday:
    print("Monday has the highest steps with", total_monday, "steps.")
elif total_tuesday > total_monday and total_tuesday > total_wednesday:
    print("Tuesday has the highest steps with", total_tuesday, "steps.")
else:
    print("Wednesday has the highest steps with", total_wednesday, "steps.")
