import json


class Reader:

    def read_all_notes(self):
        with open(r'Notebook.json', 'r', encoding='utf-8') as f:
            loaded_user_notes = json.load(f)

        return loaded_user_notes

# if __name__ == '__main__':
#     search = Reader().get_contact_surname('Петров')
