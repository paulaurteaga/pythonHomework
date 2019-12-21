import pandas as pd
import sys
import statistics
print("-----------------------")
changes=[]
dataset=pd.read_csv("Resources/budget_data.csv")
months=len(dataset["Date"].unique())
print(f'Total months:' + str(months))
netAmount=dataset["Profit/Losses"].sum()
print(f'Total:' + str(netAmount))   
increase=[]
decrease=[]
for i in range(len(dataset)-1):
    if dataset["Profit/Losses"][i]<dataset["Profit/Losses"][i+1]:
        increase.append(dataset["Profit/Losses"][i+1]-dataset["Profit/Losses"][i])
        changes.append(dataset["Profit/Losses"][i+1]-dataset["Profit/Losses"][i])
    else:
        decrease.append(dataset["Profit/Losses"][i+1]-dataset["Profit/Losses"][i])
        changes.append(dataset["Profit/Losses"][i+1]-dataset["Profit/Losses"][i])
   
maximun=max(increase)
minimun=min(decrease)
average=statistics.mean(changes)
print(f'Average Change:' + str(average))
for x in range(len(dataset)-1):
    if dataset["Profit/Losses"][x+1]-dataset["Profit/Losses"][x]==maximun:
        greatIncInd=x+1
    elif dataset["Profit/Losses"][x+1]-dataset["Profit/Losses"][x]==minimun:
        greatDecInd=x+1
dateIncrease=dataset["Date"][greatIncInd]
dateDecrease=dataset["Date"][greatDecInd]
print(f'Greatest Increase in Profits: ' + dateIncrease + str(" ") +  str(maximun) )
print(f'Greatest Decrease in Profits: ' + dateDecrease + str(" ") +  str(minimun) )
sys.stdout = open("solution.txt", "w")
print("-----------------------")
print(f'Total months:' + str(months))
print(f'Total:' + str(netAmount))    
print(f'Average Change:' + str(average))
print(f'Greatest Increase in Profits: ' + dateIncrease + str(" ") +  str(maximun) )
print(f'Greatest Decrease in Profits: ' + dateDecrease + str(" ") +  str(minimun) )