# Cinema Ticket Pre-Sale Program

TOTAL_TICKETS = 20


# Function to display remaining tickets
def display_remaining_tickets(remaining):
    print("Tickets remaining:", remaining)


# Function to process ticket purchase
def buy_tickets(remaining):
    tickets = int(input("How many tickets would you like to buy? (1-4): "))

    # Check if ticket request is valid
    if tickets < 1 or tickets > 4:
        print("You can only buy between 1 and 4 tickets.")
    elif tickets > remaining:
        print("Not enough tickets remaining.")
    else:
        remaining = remaining - tickets
        return remaining, True

    return remaining, False


# Main function
def main():

    remaining_tickets = TOTAL_TICKETS
    buyer_count = 0   # accumulator

    # Loop until all tickets are sold
    while remaining_tickets > 0:

        display_remaining_tickets(remaining_tickets)

        remaining_tickets, success = buy_tickets(remaining_tickets)

        # Count buyers only if purchase was successful
        if success:
            buyer_count += 1

        print()

    # Output final results
    print("All tickets have been sold!")
    print("Total number of buyers:", buyer_count)


# Call the main function
main()
