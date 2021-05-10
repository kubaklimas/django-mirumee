from books.models import Book
from django.core.management.base import BaseCommand
from csv import reader

class Command(BaseCommand):
    help = 'Read books from csv file'

    def add_arguments(self, parser):
        parser.add_argument('--load', type=str, help='Read from csv')

    def handle(self,*args, **kwargs):
        load = kwargs['load']
        with open(load, 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            if header != None:
                for row in csv_reader:
                    data = row[0].split(';')
                    Book.objects.create(
                        isbn=data[0],
                        title=data[1],
                        author=data[2],
                        genre=data[3]
                        )
                    