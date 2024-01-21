from django.db import models

class Booking(models.Model):
    """ BookTable model """

    name = models.CharField(max_length=50, blank=False)

    email =models.EmailField(blank=False)

    phone = models.CharField(max_length=20, blank=False)
    
    no_of_people = models.IntegerField(blank=False)
    
    message = models.CharField(max_length=250, blank=True)

    models.ManyToManyField('Table', through='BookingTable')

class Table(models.Model):
    """ Table Model """

    number = models.IntegerField(blank=False)

    no_of_seats = models.IntegerField(blank=False)

    def __str__(self) -> str:
        return "number: {}, number of seats: {}".format(self.number, self.no_of_seats)

class BookingTable(models.Model):
    """" Booking Table """

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    
    booking_date = models.DateField(blank=False)

    booking_time = models.TimeField(blank=False) 

    def __str__(self) -> str:
        return "date: {}, time: {}".format(self.booking_date, self.booking_time);


