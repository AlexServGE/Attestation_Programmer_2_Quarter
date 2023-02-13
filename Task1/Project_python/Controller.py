from Writer import Writer
from Reader import Reader
from Viewer import Viewer



class Controller:

    def __init__(self):
        print('Вас приветствует приложение: Справочник\n')
        self.writer = Writer()
        self.reader = Reader()
        self.viewer = Viewer()
        self.session_start()

    def session_start(self):
        while self.viewer.selection != '6':
            self.viewer.show_menu()
            if self.viewer.selection == '1':
                all_notes = self.reader.read_all_notes()
                self.viewer.show_all_notes(all_notes)
            elif self.viewer.selection == '2':
                self.viewer.show_write_menu()
                for i in range(self.viewer.selection):
                    self.writer.note_create_and_save()
            # # elif self.viewer.selection == '2':
            #     self.viewer.show_contact_by_surname()
            #     self.reader.get_contact_surname(self.viewer.selection)
