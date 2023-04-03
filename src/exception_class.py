class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else "Неизвестная ошибка содержания файла csv"

    def __str__(self):
        return self.message
