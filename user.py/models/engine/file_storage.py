#!/usr/bin/python3
...
def reload(self):
    """Deserializes the JSON file to __objects."""
    try:
        with open(self.__file_path, 'r') as f:
            obj_dict = json.load(f)
        for obj_id, obj_attrs in obj_dict.items():
            cls_name = obj_attrs['__class__']
            cls = eval(cls_name)  # Use eval to get the class from its name
            self.__objects[obj_id] = cls(**obj_attrs)
    except FileNotFoundError:
        pass

