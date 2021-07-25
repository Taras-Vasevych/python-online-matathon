def filterBible(scripture, book, chapter):
    return[
        book_id
        for book_id in scripture
        if book_id[0:2] == book and book_id[2:5] == chapter
    ]
