import os
import csv
from collections import OrderedDict
from operator import itemgetter


csvpath = os.path.join('..', "Resources", "election_data.csv")

votes = 0
winner = 0
total_candidates = 0
greatest_votes = ["", 0]
group = []
candidate_votes = {}


with open (csvpath) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]

        if row["Candidate"] not in group:
            group.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1

        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(votes))



    for candidate in candidate_votes:
        print(candidate + ": " + str(((candidate_votes[candidate]/votes)*100)) + "%" + " (" + str(candidate_votes[candidate]) + ")")
        candidate_results = (candidate + " " + str(((candidate_votes[candidate]/votes)*100)) + '%' + " (" + str(candidate_votes[candidate]) + ")")

winner = sorted(candidate_votes.items(), key =itemgetter(1), reverse =True)

print()
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes))
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")


