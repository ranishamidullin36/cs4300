from src.task5 import books_authors, student_db

# perform some tests to verify that it is an array with 2 elements per index that contains string
def test_books_authors():
    assert isinstance(books_authors, list)
    assert isinstance(books_authors[0], tuple)
    for title, author in books_authors:
        assert isinstance(title, str)
        assert isinstance(author, str)

# verify that its a dictionary(database) and that the database contains string for the names and intiger for the ID's
def test_student_db():
    assert isinstance(student_db, dict)
    for key, val in student_db.items():
        assert isinstance(key, str)
        assert isinstance(val, int)