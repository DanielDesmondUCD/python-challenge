
import os
import csv


csvfile = os.path.join('Resources', 'budget_data.csv')



totalmonths = 0
totalprofit = 0
previousvalue = 0
difference = 0
gain = ["",0]
loss= ["",0]

value_change = []


with open(csvfile) as budget_data:
    reader = csv.DictReader(budget_data)

    
    for row in reader:

        
        totalmonths += 1
        totalprofit += int(row["Profit/Losses"])
        

        
        difference = int(row["Profit/Losses"]) - previousvalue
        

        
        previousvalue = int(row["Profit/Losses"])
       

       
        if (difference > gain[1]):
            gain[1] = difference
            gain[0] = row["Date"]

        if (difference < loss[1]):
            loss[1] = difference
            loss[0] = row["Date"]

       
        value_change.append(int(row["Profit/Losses"]))

   
    average = sum(value_change) / len(value_change)

    
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(totalmonths))
    print("Total Revenue: " + "$" + str(totalprofit))
    print("Average Change: " + "$" + str(round(sum(value_change) / len(value_change),2)))
    print("Greatest Increase: " + str(gain[0]) + " ($" +  str(gain[1]) + ")") 
    print("Greatest Decrease: " + str(loss[0]) + " ($" +  str(loss[1]) + ")")
    
    
    data_output = os.path.join("Analysis", "hw1.txt")

    with open(data_output, "w+") as txt_file:
        txt_file.write("Total Months: " + str(totalmonths))
        txt_file.write("Total Revenue: " + "$" + str(totalprofit))
        txt_file.write("Average Change: " + "$" + str(round(sum(value_change) / len(value_change),2)))
        txt_file.write("Greatest Increase: " + str(gain[0]) + " ($" +  str(gain[1]) + ")") 
        txt_file.write("Greatest Decrease: " + str(loss[0]) + " ($" +  str(loss[1]) + ")")


