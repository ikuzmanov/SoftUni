from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.get_object(category_id, self.categories)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.get_object(topic_id, self.topics)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_object(document_id, self.documents)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.get_object(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_object(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.get_object(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.get_object(document_id, self.documents)
        return document

    @staticmethod
    def get_object(id, obj_location):
        for obj in obj_location:
            if obj.id == id:
                return obj

    def __repr__(self):
        return f'\n'.join(doc.__repr__() for doc in self.documents)
