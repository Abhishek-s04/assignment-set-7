'''Write a python program to help an airport manager to generate few statistics based on the ticket details available for a day.
Go through the below program and complete it based on the comments mentioned in it.
Note: Perform case sensitive string comparisons wherever necessary.
'''
# Sample ticket list - format: "flight_no:source:destination:ticket_no"
# ticket_list holds ticket details for a day
ticket_list = [
    "AI567:MUM:LON:014", "AI077:MUM:LON:056", "BA896:MUM:LON:067", 
    "SI267:MUM:SIN:145", "AI077:MUM:CAN:060", "SI267:BLR:MUM:148", 
    "AI567:CHE:SIN:015", "AI077:MUM:SIN:050", "AI077:MUM:LON:051", 
    "SI267:MUM:SIN:146"
]

def find_passengers_flight(airline_name="AI"):
    """This function finds and returns the number of passengers 
    traveling in the specified airline."""
    count = 0
    for ticket in ticket_list:
        # Splitting each ticket detail into flight_no, source, destination, and ticket_no
        flight_details = ticket.split(":")
        # Check if the flight number starts with the specified airline_name
        if flight_details[0].startswith(airline_name):
            count += 1
    return count

def find_passengers_destination(destination):
    """This function finds and returns the number of passengers 
    traveling to the specified destination."""
    count = 0
    for ticket in ticket_list:
        # Splitting the ticket detail
        flight_details = ticket.split(":")
        # Check if the destination matches the specified destination
        if flight_details[2] == destination:
            count += 1
    return count

def find_passengers_per_flight():
    """This function finds and returns a list with the number of passengers 
    traveling on each flight.
    The format of the list is [flight_no:no_of_passengers, ...]."""
    flight_dict = {}
    for ticket in ticket_list:
        # Splitting the ticket to get flight number
        flight_details = ticket.split(":")
        flight_no = flight_details[0]
        # If the flight_no is already in the dictionary, increment the count
        if flight_no in flight_dict:
            flight_dict[flight_no] += 1
        else:
            # If flight_no is encountered for the first time, set its count to 1
            flight_dict[flight_no] = 1
    
    # Converting the dictionary to a list in the specified format
    flight_list = [f"{flight}:{count}" for flight, count in flight_dict.items()]
    return flight_list

def sort_passenger_list():
    """This function sorts the list of passengers per flight in descending 
    order of the number of passengers."""
    # First, get the list of passengers per flight
    flight_list = find_passengers_per_flight()
    
    # Sort the flight list based on the number of passengers, which is the part after ':'
    sorted_list = sorted(flight_list, key=lambda x: int(x.split(":")[1]), reverse=True)
    
    return sorted_list

# Test the functions with different inputs
print(find_passengers_flight("AI"))  # Number of passengers in airline "AI"
print(find_passengers_destination("LON"))  # Number of passengers traveling to "LON"
print(find_passengers_per_flight())  # Passengers per flight in the specified format
print(sort_passenger_list())  # Sorted list based on the number of passengers per flight
