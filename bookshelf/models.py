from django.db import models

class Author (models.Model):

    Name = models.CharField (max_length=200)
    Surname = models.CharField (max_length=200)

class Book (models.Model):

    Image = models.ImageField (default="")
    Title = models.CharField (max_length=200)
    Description = models.TextField (blank=False)

    Authors = models.ManyToManyField (Author, through="Book_Author_Link")

class Tag (models.Model):

    TagName = models.CharField (max_length=200)

class Book_Author_Link (models.Model):

    Author_Key = models.ForeignKey (Author, on_delete=models.CASCADE)
    Book_Key = models.ForeignKey (Book, on_delete=models.CASCADE)

class Book_Tag_Link (models.Model):

    Tag_Key = models.ForeignKey (Tag, on_delete=models.CASCADE)
    Book_Key = models.ForeignKey (Book, on_delete=models.CASCADE)
