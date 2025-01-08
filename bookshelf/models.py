from django.db import models
from django.utils import timezone

class Author (models.Model):

    Name = models.CharField (max_length=200)
    Surname = models.CharField (max_length=200)

    def __str__(self):
        return self.Name + " " + self.Surname

class Tag (models.Model):

    TagName = models.CharField (max_length=200)

    def __str__(self):
        return self.TagName

class Book (models.Model):

    Image = models.ImageField (default="")
    Title = models.CharField (max_length=200, unique=True)
    Description = models.TextField (blank=False)
    Added = models.DateField (default=timezone.now)

    Authors = models.ManyToManyField (Author, through="Book_Author_Link")
    Tags = models.ManyToManyField (Tag, through='Book_Tag_Link')

    def __str__(self):
        return self.Title

class Book_Author_Link (models.Model):

    Author_Key = models.ForeignKey (Author, on_delete=models.CASCADE)
    Book_Key = models.ForeignKey (Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.Book_Key.Title + " -> " + self.Author_Key.Name + " " + self.Author_Key.Surname


class Book_Tag_Link (models.Model):

    Tag_Key = models.ForeignKey (Tag, on_delete=models.CASCADE)
    Book_Key = models.ForeignKey (Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.Book_Key.Title + " -> " + self.Tag_Key.TagName
