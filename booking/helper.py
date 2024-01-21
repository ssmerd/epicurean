from .models import Booking, BookingTable, Table
from datetime import datetime, timedelta


class BookingHelper():
    """ Booking helper class """

    def __init__(self,form):
        self.form = form

    def save_booking(self):
        """ The method saves the booking to the database. Bookings are for one hour. """
        
        booking = Booking()

        booking.name = self.form.cleaned_data["name"]
        booking.email = self.form.cleaned_data["email"]
        booking.phone = self.form.cleaned_data["phone"]
        booking.no_of_people = self.form.cleaned_data["no_of_people"]
        booking.message = self.form.cleaned_data["message"]

        booking_date = self.form.cleaned_data["date"]
        booking_time = self.form.cleaned_data["time"]

        booking_time = datetime.strptime(booking_time, '%H:%M')
        booking_time_delta = booking_time + timedelta(minutes=30)
        booking_time = booking_time.time()
        booking_time_delta = booking_time_delta.time()

        
        tables = Table.objects.all().order_by('no_of_seats')
        
        # This excerpts look for a free table.
        for table in tables:
          
            free_table_1 = table.bookingtable_set.filter(booking_date=booking_date, booking_time=booking_time)
            free_table_2 = table.bookingtable_set.filter(booking_date=booking_date, booking_time=booking_time_delta)

            if not (free_table_1 or free_table_2):
                if table.no_of_seats >= booking.no_of_people:
                    self.book_table(booking, table, booking_date, booking_time)
                    self.book_table(booking, table, booking_date, booking_time_delta)
                    return True
            
            
        # This code look for more tables

        tables = Table.objects.all().order_by('-no_of_seats')
        
        table_list = []

        for table in tables:
      
            free_table_1 = table.bookingtable_set.filter(booking_date=booking_date, booking_time=booking_time)
            free_table_2 = table.bookingtable_set.filter(booking_date=booking_date, booking_time=booking_time_delta)

            if not (free_table_1 or free_table_2):
                table_list.append(table)

        t = []
        seats = 0

        for table in table_list:
            if seats <= booking.no_of_people:
                seats += table.no_of_seats
                t.append(table)
           
        if seats >= booking.no_of_people:
            self.book_tables(booking, t, booking_date, booking_time)
            self.book_tables(booking, t, booking_date, booking_time_delta)
            return True
     

        return False

    def book_table(self, booking, table, booking_date, booking_time):
        """ Book a table """
        
        booking_table = BookingTable(booking=booking, table=table, booking_date=booking_date, booking_time=booking_time)

        booking.save()
        booking_table.save()
        
    
    def book_tables(self, booking, tables, booking_date, booking_time):
        """ Book multipe tables """

        booking.save()

        for table in tables:
            booking_table = BookingTable(booking=booking, table=table, booking_date=booking_date, booking_time=booking_time)
            booking_table.save()
        