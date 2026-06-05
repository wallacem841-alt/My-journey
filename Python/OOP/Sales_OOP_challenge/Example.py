from pathlib import Path
class Chapter:
    def __init__(self, path: Path):
        self.path = path
        self.text = path.read_text(encoding="utf-8")

    @property
    def word_count(self):
        return len(self.text.split())


class Book:
    def __init__(self, title: str):
        self.title = title
        self.chapters = []

    def add_chapter(self, chapter: Chapter):
        self.chapters.append(chapter)

    @property
    def word_count(self):
        return sum(c.word_count for c in self.chapters)

book = Book("My Book")

book_dir = Path("Book")

for md_file in sorted(book_dir.glob("*.md")):
    chapter = Chapter(md_file)
    book.add_chapter(chapter)

print(book.word_count)