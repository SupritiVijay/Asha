import pandas as pd

cols = ['Description','Name','Location',"Time"]
df = pd.DataFrame({col:[] for col in cols})
df.to_csv("complaint.csv", index=False)