
class Ticket:
    def __init__(self, movie_name, show_time, seat_number, ticket_price):
        self.movie_name = movie_name
        self.show_time = show_time
        self.seat_number = seat_number
        self.ticket_price = ticket_price

  
    def display_ticket(self):
        print("Movie Name :", self.movie_name)
        print("Show Time  :", self.show_time)
        print("Seat No    :", self.seat_number)
        print("Price      : ₹", self.ticket_price)
        print("-" * 30)

  
    def get_price(self):
        return self.ticket_price



tickets = []


n = int(input("Enter number of tickets to book: "))


for i in range(n):
    print(f"\nEnter details for Ticket {i + 1}:")
    movie = input("Movie name: ")
    time = input("Show time: ")
    seat = input("Seat number: ")
    price = float(input("Ticket price: "))

    ticket = Ticket(movie, time, seat, price)
    tickets.append(ticket)

total_amount = 0
print("\n--- Ticket Details ---")
for t in tickets:
    t.display_ticket()
    total_amount += t.get_price()

print("Total amount to be paid: ₹", total_amount)