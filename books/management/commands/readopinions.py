from books.models import Opinion, Book
from django.core.management.base import BaseCommand
from csv import reader

class Command(BaseCommand):
    help = 'Read books from csv file'

    def add_arguments(self, parser):
        parser.add_argument('--load', type=str, help='Read from csv')

    def handle(self,*args, **kwargs):
        load = kwargs['load']
        #all_books =  Book.objects.all()
        with open(load, 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            if header != None:
                for row in csv_reader:
                    data = row[0].split(';')
                    book = Book.objects.get(isbn=data[0])
                    Opinion.objects.create(
                        isbn=book,
                        mark=data[1],
                        comment=data[2]
                        )
                    