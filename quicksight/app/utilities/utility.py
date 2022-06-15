class Struct:
    def __init__(self, json_data):
        self.convert(json_data)

    def convert(self, json_data):
        if not isinstance(json_data, dict):
            return
        for key in json_data:
            if not isinstance(json_data[key], dict):
                self.__dict__.update({key: json_data[key]})
            else:
                self.__dict__.update({ key: Struct(json_data[key])})

#TODO: broken
class Destruct:
    def __init__(self, json_data):
        self.convert(json_data)

    def convert(self, json_data):
        if isinstance(json_data, dict):
            return
        for key in json_data:
            if isinstance(json_data[key], dict):
                self.__dict__.update({key: json_data[key]})
            else:
                self.__dict__.update({ key: Struct(json_data[key])})