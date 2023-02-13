class Viewer:

    def __init__(self):
        self.selection = None

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

    def show_write_menu(self):
        self.selection = int(input('Сколько заметок требуется создать [1/2/..]: '))

    def show_all_notes(self, all_notes):
        for key_1, val_1 in all_notes.items():
            print(f'Заголовок заметки:{key_1}')
            for key_2, val_2 in val_1.items():
                print(f'\t{key_2}: {val_2}')
        print(100*'>')
