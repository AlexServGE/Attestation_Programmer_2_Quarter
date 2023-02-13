import json
import datetime


class Note:

    # def __init__(self, title, body, time_created, time_updated):
    #     self.title = title
    #     self.body = body
    #     self.time_created = time_created
    #     self.time_updated = time_updated
    #     self.note = {self.title: (self.body, self.time_created, self.time_updated)}

    def __init__(self):
        self.title = None
        self.body = None
        self.time_created = None
        self.time_updated = None
        self.note = {self.title: {'Текст': self.body, 'Время создания': self.time_created, 'Время обновления': self.time_updated}}

    def create_note(self):
        self.title = input('Введите заголовок заметки:')
        self.body = input('Введите текст заметки:')
        self.time_created = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.time_updated = '-'
        self.note = {self.title: {'Текст': self.body, 'Время создания': self.time_created, 'Время обновления': self.time_updated}}

    # def update_note(self):
    #     print(self.title)
    #     self.title = {'Заголовок заметки': self.title['Заголовок заметки'] + input('Введите заголовок заметки:')}
    #     self.body = {'Текст заметки': input('Введите текст заметки:')}
    #     self.time_updated = {'Время обновления заметки': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
    #     self.note = {'Заметка': (self.title, self.body, self.time_created, self.time_updated)}

    # def delete_note(self):

    # def __str__(self):
    #     return f'{self.title}' \
    #            f'{self.body}' \
    #            f'{self.time_created}' \
    #            f'{self.time_updated}'


class Writer:

    def note_create_and_save(self):
        with open(r'Notebook.json', 'r', encoding='utf-8') as user_notes_storage:
            user_notebook = json.load(user_notes_storage)

        user_note = Note()
        user_note.create_note()
        user_notebook.update(user_note.note)

        with open(r'Notebook.json', 'w', encoding='utf-8') as user_notes_storage:
            json.dump(user_notebook, user_notes_storage)


if __name__ == '__main__':
    user_note = Note().create_note()
