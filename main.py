
from table import Table
from fields import StringField

class Book(Table):
    title = StringField()
author = StringField()


if __name__=="__main__":

    book1 = Book(title="2022", author="malshan")
    print(book1)
