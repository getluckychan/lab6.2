class Sign(Exception):
    def __init__(self):
        self.massage = None

    def __str__(self):
        self.massage = "Введіть + або - або нічого"
        return self.massage

