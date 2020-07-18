#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ticket_cache = {}
    route = []

    for ticket in tickets:
        if ticket.source not in ticket_cache:
            ticket_cache[ticket.source] = ticket.destination

    route.append(ticket_cache["NONE"])

    current_destination = route[0]

    while current_destination != "NONE":
        current_destination = ticket_cache[current_destination]
        route.append(current_destination)
    
    # Your code here

    return route

# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# reconstruct_trip(tickets, 3)