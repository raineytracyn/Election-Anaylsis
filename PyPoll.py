#The data we need to retrieve
# Open the election results and read the file.
election_results= 'Resources/election_results.csv'
election_data = open(election_results, 'r')
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
with open(election_results) as election_data:
# To do: perform analysis.
    print(election_data)
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The precentage of votes each candidate won
#4. The total number of votes each candidiate won
#5. The winner of the election based on popular vote
# Close the file.
election_data.close()


