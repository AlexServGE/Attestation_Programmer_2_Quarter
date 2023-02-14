from NoteWriter import Writer
from NoteReader import Reader
from NoteRemover import NoteRemover
from Viewer import Viewer


class Controller:

    def __init__(self):
        print('Вас приветствует приложение: Справочник\n')
        self.note_writer = Writer()
        self.note_reader = Reader()
        self.viewer = Viewer()
        self.note_remover = NoteRemover()
        self.session_start()

    def session_start(self):
        while self.viewer.selection != '5':
            self.viewer.show_menu()
            if self.viewer.selection == '1':
                all_notes = self.note_reader.read_all_notes()
                self.viewer.show_all_notes(all_notes)
                self.viewer.selection = None
            elif self.viewer.selection == '2':
                self.viewer.show_write_menu()
                for i in range(self.viewer.selection):
                    self.note_writer.note_create_and_save()
                self.viewer.selection = None
            elif self.viewer.selection == '3':
                all_notes = self.note_reader.read_all_notes()
                self.viewer.show_update_note_menu(all_notes)
                if (self.viewer.selection == 1):
                    self.note_writer.note_update_and_save(all_notes, self.viewer.idx_note_to_update)
                    self.note_writer.notes_save(self.note_writer.all_notes_after_update)
                    self.viewer.idx_note_to_update, self.viewer.selection, self.note_writer.all_notes_after_update = None, None, None
            elif self.viewer.selection == '4':
                all_notes = self.note_reader.read_all_notes()
                self.viewer.show_delete_menu(all_notes)
                if (self.viewer.selection == 1):
                    self.note_remover.delete_note(all_notes, self.viewer.idx_note_to_delete)
                    self.note_writer.notes_save(self.note_remover.all_notes_after_delete)
                    self.viewer.idx_note_to_delete, self.viewer.selection = None, None
