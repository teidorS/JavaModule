"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    seats = ["A", "B", "C", "D"]
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    for index in range(number):
        if index == len(seats):
            index = index % len(seats)
        yield seats[index]
        
    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seats = ["A", "B", "C", "D"]
    current_row = 1
    seat_count = 0
    
    while seat_count < number:
        if current_row == 13:
            current_row += 1
        
        for seat in seats:
            yield f"{current_row}{seat}"
            seat_count += 1
            if seat_count >= number:
                break
        
        current_row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    all_seats = generate_seats(len(passengers))

    return {passenger: seat for passenger, seat in zip(passengers, all_seats)}
        

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        ticket_number = seat + flight_id
        no_of_trailing_zeros = 12 - len(ticket_number)
        combined_ticket_no = ticket_number + '0' * no_of_trailing_zeros
        yield combined_ticket_no
