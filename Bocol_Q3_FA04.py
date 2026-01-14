import numpy as np

arr = []

#list down their steps for 3 days
np.steps = {
  "ME": [3500, 5900, 5800],
  "LIEN": [3500, 6740, 4000],
  "KRIS": [4000, 6000, 5700]
}
print(np.steps)

#total for each row
total_me = sum(np.steps["ME"])
total_lien = sum(np.steps["LIEN"])
total_kris = sum(np.steps["KRIS"])

print("Total steps for ME:", total_me)
print("Total steps for LIEN:", total_lien)
print("Total steps for KRIS:", total_kris)

#Identify who has the highest steps lol
if total_me > total_lien and total_me > total_kris:
    print("Me has the highest steps with", total_me, "steps.")
elif total_lien > total_me and total_lien > total_kris:
    print("Lien has the highest steps with", total_lien, "steps.")
else:
    print("Kris has the highest steps with", total_kris, "steps.")
    
#difference between the highest total steps and the lowest total steps
totals = [total_me, total_lien, total_kris]
difference = max(totals) - min(totals)
print("the difference between highest and lowest total steps is:", difference, "steps.")
