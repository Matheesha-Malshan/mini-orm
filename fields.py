class Field:
    def __init__(self, field_type):
        self.field_type = field_type

class StringField(Field):
    def __init__(self):
        super().__init__('string')