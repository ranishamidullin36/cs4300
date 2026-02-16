from src.task5 import books_authors, student_db

def test_books_authors():
    assert isinstance(books_authors, list)
    assert isinstance(books_authors[0], tuple)
    for title, author in books_authors:
        assert isinstance(title, str)
        assert isinstance(author, str)

def test_student_db():
    assert isinstance(student_db, dict)
    for key, val in student_db.items():
        assert isinstance(key, str)
        assert isinstance(val, int)