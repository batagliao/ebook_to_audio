from dataclasses import dataclass


@dataclass
class Book:
    def __init__(self):
        pass

    cover: bytes
    title: str
    author: str
    chapters: list[str]