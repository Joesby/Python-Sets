our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#Task 1: Flight Route Comparison
#Create a variable to find destinations both airlines fly to
shared_destinations = our_routes.intersection(competitor_routes)
#A variable unique to our airline only
our_destinations = our_routes.difference(competitor_routes)
#And a variable that neither airline has in common
unique_destinations = our_routes.symmetric_difference(competitor_routes)

#display the results in a readable fashion
print("These destinations are shared by both airlines: ", shared_destinations)
print("These destinations are only available with our airline: ", our_destinations)
print("These are the destinations that neither airline have in common: ", unique_destinations)