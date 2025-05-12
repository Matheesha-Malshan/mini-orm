from metaclass import TableMeta

class Table(metaclass=TableMeta):
    def __init__(self, **kwargs):
        
        self._data = {}
      
        for field_name in self._fields:
            if field_name in kwargs:
                self._data[field_name] = kwargs[field_name]
            else:
                self._data[field_name] = None  # optional: default None

     
        for key in kwargs:
            if key not in self._fields:
                raise AttributeError(f"Invalid field '{key}' for table '{self._table_name}'")

    def __repr__(self):
        field_values = ', '.join(f"{k}={v!r}" for k, v in self._data.items())
        return f"<{self._table_name} {field_values}>"
