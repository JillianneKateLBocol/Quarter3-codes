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

#average for each row
avg_me = np.mean(np.steps["ME"])
avg_lien = np.mean(np.steps["LIEN"])
avg_kris = np.mean(np.steps["KRIS"])

#total sum of all steps
total_steps = total_me + total_lien + total_kris
print("Our combined total steps:", total_steps)
