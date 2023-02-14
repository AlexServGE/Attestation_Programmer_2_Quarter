class NoteRemover:

    def __init__(self):
        self.all_notes_after_delete = None

    def delete_note(self, all_notes, idx_note_to_delete):
        self.all_notes_after_delete = {key: val for idx, key, val in
                                       zip(range(1, len(all_notes.keys()) + 1), all_notes.keys(), all_notes.values()) if
                                       idx != idx_note_to_delete}
