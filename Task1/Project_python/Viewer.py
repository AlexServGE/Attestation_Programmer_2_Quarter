class Viewer:

    def __init__(self):
        self.selection = None
        self.idx_note_to_delete = None
        self.idx_note_to_update = None

    def show_menu(self):
        selection = input('Выберите действие:\n '
                          '1. Просмотреть список всех заметок\n '
                          '2. Создать новую заметку\n '
                          '3. Изменить заметку\n '
                          '4. Удалить заметку\n '
                          '5. Закончить работу\n '
                          'Укажите свой выбор [1/2/3/4/5]: ')
        print(100 * '>')
        self.selection = selection

    def show_all_notes(self, all_notes):
        for idx, key_1, val_1 in zip(range(1, len(all_notes.keys()) + 1), all_notes.keys(), all_notes.values()):
            print(f'{idx} Заголовок заметки:{key_1}')
            for key_2, val_2 in val_1.items():
                print(f'\t{key_2}: {val_2}')
        print(100 * '>')

    def show_write_menu(self):
        self.selection = int(input('Сколько заметок требуется создать [1/2/..]: '))
        print(100 * '>')

    def show_update_note_menu(self, all_notes):
        self.show_all_notes(all_notes)
        self.idx_note_to_update = int(
            input('Укажите порядковый номер заметки, которую Вы хотели бы отредактировать [1/2/..]: '))
        for idx, key_1, val_1 in zip(range(1, len(all_notes.keys()) + 1), all_notes.keys(), all_notes.values()):
            if idx == self.idx_note_to_update:
                print(f'{idx} (Выбрана заметки для редактирования) Заголовок заметки:{key_1}')
            else:
                print(f'{idx} Заголовок заметки:{key_1}')
            for key_2, val_2 in val_1.items():
                print(f'\t{key_2}: {val_2}')
        print(100 * '>')
        self.selection = 1 if input(f'Подтвердите запрос на редактирование заметки под номером {self.idx_note_to_update}\n '
                                    f'отредактировать выбранную заметку [да]\n'
                                    f'выйти в стартовое меню [нет]:') == 'да' else 0
        if self.selection == 0: self.idx_note_to_delete = None

    def show_delete_menu(self, all_notes):
        self.show_all_notes(all_notes)
        self.idx_note_to_delete = int(
            input('Укажите порядковый номер заметки, которую Вы хотели бы удалить [1/2/..]: '))
        for idx, key_1, val_1 in zip(range(1, len(all_notes.keys()) + 1), all_notes.keys(), all_notes.values()):
            if idx == self.idx_note_to_delete:
                print(f'{idx} (Выбрана заметки для удаления) Заголовок заметки:{key_1}')
            else:
                print(f'{idx} Заголовок заметки:{key_1}')
            for key_2, val_2 in val_1.items():
                print(f'\t{key_2}: {val_2}')
        print(100 * '>')
        self.selection = 1 if input(f'Подтвердите запрос на удаление заметки под номером {self.idx_note_to_delete}\n '
                                    f'удалить выбранную заметку [да]\n'
                                    f'выйти в стартовое меню [нет]:') == 'да' else 0
        if self.selection == 0: self.idx_note_to_delete = None


