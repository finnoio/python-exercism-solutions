"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = ["A", "B", "C", "D"]
    for i in range(number):
        yield letters[i % len(letters)]



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
    seats_per_row = 4
    seats_left = number
    max_row = number // seats_per_row

    for i in range(max(1, max_row + int(number > 12 * 4) + 1)):
        row_num = i+1
        if row_num != 13:
            for j in generate_seat_letters(min(seats_per_row, seats_left)):
                seats_left -= 1
                yield str(row_num) + str(j)



def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    ticket_len = 12
    for seat in seat_numbers:
        sf_part = seat + flight_id
        zero_part = '0'*(ticket_len - len(sf_part))
        yield sf_part + zero_part
