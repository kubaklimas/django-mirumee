from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Book(models.Model):
    class Author(models.TextChoices):
        sinicka= _("Alicja Sinicka")
        coben = _("Harlan Coben")
        mroz = _("Remigiusz Mróz")
        collins= _("Suzanne Collins")
        wolf= _("Anna Wolf")
        '''
            Autor musiałby być oddzielnym modelem, żeby zastosować 
            OneToOne field. Nie wiem czy sposób który zastosowałem 
            żeby to ominąc jest najlepszy ale dziala.
        '''
    isbn = models.PositiveBigIntegerField()
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50,choices = Author.choices, default= Author.coben)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return "%s"%self.isbn
    
    
class Opinion(models.Model):
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    mark = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.CharField(max_length=250)

    def __str__(self):
        return self.isbn
    