class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price) -> None:
        self.movie_title = movie_title
        self.seat_number  = seat_number
        self.price = price

        MovieTicket.total_tickets_sold +=1

    def display_info(self):
        print(f"Movie Title {self.movie_title}")
        print(f"Your seat number {self.seat_number}")
        print(f"Price is {self.price}")


Ticket1 = MovieTicket("Doomsday", 23, 12)
Ticket2 = MovieTicket("Avatar 3", 20, 11)

print(MovieTicket.total_tickets_sold)
Ticket1.display_info()
print("="*20)
Ticket2.display_info()

