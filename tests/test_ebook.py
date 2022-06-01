from ebooklib import epub

import src.ebook

def test_loadbook():
    b = src.ebook.load_ebook("tests/resources/pg1661.epub")
    assert b is not None
    assert b.cover is not None
    assert b.title == 'The Adventures of Sherlock Holmes'

def test_getcover():
    b = epub.read_epub("tests/resources/pg1661.epub")
    cover = src.ebook.get_cover(b)
    assert cover is not None
    assert isinstance(cover, bytes)

def test_gettitle():
    b = epub.read_epub("tests/resources/pg1661.epub")
    title = src.ebook.get_title(b)
    assert title is not None
    assert title == 'The Adventures of Sherlock Holmes'

def test_getauthor():
    b = epub.read_epub("tests/resources/pg1661.epub")
    author = src.ebook.get_author(b)
    assert author is not None
    assert author == 'Arthur Conan Doyle'

def test_getchapters():
    b = epub.read_epub("tests/resources/pg1661.epub")
    chapters = src.ebook.get_chapters(b)
    assert chapters is not None
    assert len(chapters) > 0