# <ins> Overview of Election Audit </ins>
### Purpose of this election audit analysis is to determine:
  * The voter turnout for each county
  * The percentage of votes from each county out of the total count
  * The county with the highest turnout
### Additional information which can be obtained includes the winner of the election, evaluate which candidates were strongest where, as well as why and by how much.
# <ins> Election-Audit Results </ins>
### Without diving too deep, you can see below our winner is Ms. Diana DeGette, taking the election by storm with 73.8% of ballots casted selecting her.
###### ![Election_Results](https://github.com/raineytracyn/Election-Anaylsis/blob/main/Resources/Election%20Results.png)
### Lets take a deeper look into what happened:
###### ![Details_of_the_election_results](https://github.com/raineytracyn/Election-Anaylsis/blob/main/Resources/Details%20of%20the%20election%20results.png)
1. Arapahoe
    * In the county of Arapahoe, 24,801 votes were casted, with a little over 63% of the votes being for Ms. DeGette. Mr. Stockham trailed in second place with 8,302 votes casted. This county accounted for 6.71% of the total votes casted between the three counties, making it the smallest in casted votes between the three counties.
2. Denver
    * In the county of Denver, 306,055 votes were casted, with a little over 78% of the votes being for Ms. DeGette. Mr. Stockham trailed in second place with 57,188 votes casted. This county accounted for 82.78% of the total votes casted between the three counties, making it the largest in casted votes between the three counties. As you can see in “Election Results”, Ms. DeGette holds the largest percentage of votes (74%), a little over 64% of that coming from Denver county alone.
3. Jefferson
    * In the county of Jefferson, 38,855 votes were casted, with a little over 5% of the votes being for Mr. Stockham. Ms. DeGette trailed in second place with 17,963 votes casted. This county accounted for 10.51% of the total votes casted between the three counties, making it the second smallest in casted votes between the three counties. 
    * An item to note with Jefferson county that would be good to deep dive into is Mr. Stockham held a .47% lead over Ms. DeGette, which wasn’t much. What political areas are unique to Jefferson county that assisted Mr. Stockham in taking the lead? Did Mr. Stockham hold a greater presence in Jefferson than the other counties? Could Mr. Stockham identify the political areas that helped him, and utilize those areas in the other counties to take the lead in an upcoming election?

# <ins> Election-Audit Summary </ins>
#### In summary, Ms. DeGette won the election, with Denver's turnout being the most substantial reasoning for her victory. Without knowing the population of each county, we cannot determine the percentage of people which came to the polls. Without knowing the economic drivers in each county, we cannot determine what political standings (aka, drivers) spoke most to each county. Jefferson county was a very close call between Ms. DeGette and Mr. Stockham. Mr. Doane had little impact in all three counties. It would be good to understand why. Does he come from outside the state? Does his political agenda not meet the needs of the citizens? Did he simply not provide enough face to face time to win over votes? If the three candidates are to run next cycle, Mr. Stockham and Mr. Doane will both need to target Denver much heavier. Mr. Doane will need to focus on Arapahoe more, and Mr. DeGette will need to focus a little more in Jefferson to bring her numbers up.
## Business proposal
#### Looking below, you can see the code currently provides basic results. The election commission script can be used with some modifications for any election. Maybe along with results below, you would like to understand the political concerns by county. Some may be very concerns about impacts on defense companies, while others are concerned with impacts on small-business owner-ship. Tying concerns with results of what county voted for who will help preparation for the next election, and help better understand the needs by county.
###### ![Code_Results](https://github.com/raineytracyn/Election-Anaylsis/blob/main/Resources/Code_Results.png)
#### Lets look at two examples of how this script can be modified to be used for other elections.
1. Adding a column to capture what the leading industry is in the county.
   * In the CSV file, add a column which captures the industry the voter is working in. Add a section of code that consolidates the top two industries for each county. Look at the results of the information and compare it to the winning and loosing candidate's focuses while on tour.
2. Adding a column to capture if the voter voted during the last cycle.
   * In the CSV file, add a column which captures if the voter participated in the last cycle by county. Consolidate the tour count and length, and compare it to the turn out. Did tour counts and lengths have an impact on the turnout in a positive way? Did it in some areas, but not others? This will help adjust dollars spent on tours to ensure the dollar has a greater impact in the future.
####
