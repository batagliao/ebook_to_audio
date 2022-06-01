import ebooklib
from ebooklib import epub

from .book import Book


def load_ebook(path):
    b = epub.read_epub(path)
    mybook = Book()
    mybook.cover = get_cover(b)
    mybook.author = get_author(b)
    mybook.title = get_title(b)
    mybook.chapters = get_chapters(b)
    return mybook


def get_cover(ebook):
    """
    Get the book cover image
    :param ebook:
    :return: an array of bytes containing the cover image or None if not found
    """
    items = list(ebook.get_items_of_type(ebooklib.ITEM_COVER))
    if len(items) > 0:
        coveritem = items[0]
        return coveritem

    # not found as cover type
    metadata = ebook.get_metadata('OPF', 'cover')
    if len(metadata) > 0:
        metadata_tuple = metadata[0]
        # get the last position
        metadata_dict = metadata_tuple[-1]
        item_id = metadata_dict['content']

        item = ebook.get_item_with_id(item_id)
        item_type = type(item)
        if item and item_type == epub.EpubImage:
            return item.content

    return None


def get_title(ebook):
    metadata = ebook.get_metadata('DC', 'title')
    if len(metadata):
        metadata_tuple = metadata[0]
        content = metadata_tuple[0]
        return content

    return None


def get_author(ebook):
    metadata = ebook.get_metadata('OPF', 'author')
    if len(metadata) > 0:
        metadata_tuple = metadata[0]
        # get the last position
        metadata_dict = metadata_tuple[-1]
        content = metadata_dict['content']
        return content

    metadata = ebook.get_metadata('DC', 'creator')
    if len(metadata):
        metadata_tuple = metadata[0]
        content = metadata_tuple[0]
        return content

    return None


def get_chapters(ebook):
    """
    Get the books chapters. The content of that chapters may vary from book to book but the result should contains html tags
    :param ebook:
    :return: an array of strings representing the content of the chapters
    """
    spine = ebook.spine
    items = ebook.items
    chapters = []
    for s in spine:
        label = s[0]
        item = [x for x in items if x.id == label]
        if len(item) == 0:
            continue

        content = item[0].get_body_content()
        chapters.append(content)

    return chapters