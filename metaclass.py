from fields import Field

class TableMeta(type):
    def __new__(cls, name, bases, namespace):
        fields = {}

        for key, value in namespace.items():
            if isinstance(value, Field):
                fields[key] = value

        print(f"fields are {name}: {fields}")

        namespace['_table_name'] = name
        namespace['_fields'] = fields

        return super().__new__(cls, name, bases, namespace)
