import pandas as pd
import sys
datafile=pd.read_csv("Resources/election_data.csv")
print("Election Results")
print("--------------")
votes=len(datafile)
print(f'Total votes:' + str(votes))
print("--------------")
converted_datafile=datafile.groupby("Candidate")
converted_datafile["Candidate"].count()
final_dataframe = pd.DataFrame(converted_datafile["Candidate"].count())
final_dataframe=final_dataframe.rename(columns={'Candidate':'Votes'})
final_dataframe=final_dataframe.sort_values("Votes", ascending=False)
new_dataframe=final_dataframe
percentages=[]
for i in range(len(new_dataframe)):
    percentages.append(new_dataframe["Votes"][i]/votes)
percentages
new_dataframe.insert(1,"Percentage",percentages)
new_dataframe['Percentage'] = pd.Series(["{0:.2f}%".format(val * 100) for val in new_dataframe['Percentage']], index = new_dataframe.index)
print(new_dataframe)
print("--------")
list=new_dataframe.index.tolist()
print(f'Winner: '+ list[0])
sys.stdout = open("solution.txt", "w")
print("Election Results")
print("--------------")
print(f'Total votes:' + str(votes))
print("--------------")
print(new_dataframe)
print("--------")
print(f'Winner: '+ list[0])