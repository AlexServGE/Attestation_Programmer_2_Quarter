import json
import datetime


class Note:

    def __init__(self, title, body, time_created, time_updated):
        self.title = title
        self.body = body
        self.time_created = time_created
        self.time_updated = time_updated
        self.note = {self.title: {'Текст': self.body, 'Время создания': self.time_created, 'Время обновления': self.time_updated}}

    def create_note(self):
        self.title = input('Введите заголовок заметки:')
        self.body = input('Введите текст заметки:')
        self.time_created = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.time_updated = '-'
        self.note = {self.title: {'Текст': self.body, 'Время создания': self.time_created,
                                  'Время обновления': self.time_updated}}

    def update_note(self):
        title = input('Введите новый заголовок заметки:')
        body = input('Введите новый текст заметки:')
        time_created = self.time_created
        time_updated = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        return Note(title, body, time_created, time_updated)


class Writer:

    def __init__(self):
        self.all_notes_after_update = None

    def note_create_and_save(self):
        with open(r'Notebook.json', 'r', encoding='utf-8') as user_notes_storage:
            user_notebook = json.load(user_notes_storage)

        user_note = Note(None, None, None, None)
        user_note.create_note()
        user_notebook.update(user_note.note)

        with open(r'Notebook.json', 'w', encoding='utf-8') as user_notes_storage:
            json.dump(user_notebook, user_notes_storage)

    def note_update_and_save(self, all_notes, idx_note_to_update):
        for idx, key, val in zip(range(1, len(all_notes.keys()) + 1), all_notes.keys(), all_notes.values()):
            if idx == idx_note_to_update:
                user_note_to_update = Note(key, val['Текст'], val['Время создания'], val['Время обновления'])
                user_note_updated = user_note_to_update.update_note()
                break

        self.all_notes_after_update = {
            key if idx != idx_note_to_update else user_note_updated.title:
                val if idx != idx_note_to_update else user_note_updated.note[user_note_updated.title]
            for idx, key, val in zip(range(1, len(all_notes.keys()) + 1), all_notes.keys(), all_notes.values())}

    def notes_save(self, all_notes):
        with open(r'Notebook.json', 'w', encoding='utf-8') as user_notes_storage:
            json.dump(all_notes, user_notes_storage)


if __name__ == '__main__':
    print()
