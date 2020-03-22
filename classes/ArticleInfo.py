import re


class ArticleInfo:
    def __init__(self, link, header="", description="", category="", author="", published_at="", modified_at="", paragraphs=""):
        self.link = link
        self.header = header
        self.description = description
        self.category = category
        self.author = author
        self.published_at = published_at
        self.modified_at = modified_at
        self.paragraphs = paragraphs

    def is_populated(self):
        if not self.header:
            return False
        return True

    def __str__(self):
        return f'Link: {self.link}\nHeader:{self.header}\nDescription: {self.description}\nCategory: {self.category}\n' \
               f'Author: {self.author}\nPublished: {self.published_at}\nModified_at: {self.modified_at}' \
               f'\nParagraphs count: {len(self.paragraphs)}\n'

    def as_dict(self):
        return {'Link': self.link, 'Header': self.header, 'Description': self.description, 'Category': self.category,
                'Author': self.author, 'Published_at': self.published_at, 'Modified_at': self.modified_at,
                'Paragraphs': self.paragraphs, 'Paragraphs_count': len(self.paragraphs)}

    def words_in_all_paragraphs(self):
        """
        Returns all words in this objects paragraph
        :return: Words in list
        """
        words = []

        # regex expression takes only words from paragraph (ignores '.', '?', ..)
        for paragraph in self.paragraphs:
            words.extend(re.findall(r'\w+', paragraph))

        return words

    @staticmethod
    def db_objects_to_articles(db_objects):
        """
        Converts db_objects from database.py -> retrieve_articles()
        :param db_objects: List of dicts
        :return: List of ArticleInfo instances
        """
        articles = []

        for db_object in db_objects:
            articles.append(ArticleInfo(db_object["Link"], db_object["Header"], db_object["Description"],
                                        db_object["Category"], db_object["Author"], db_object["Published_at"],
                                        db_object["Modified_at"], db_object["Paragraphs"]))
        return articles