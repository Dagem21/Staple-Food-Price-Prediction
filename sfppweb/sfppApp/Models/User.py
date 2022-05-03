class User:
    id = None
    username = None
    password = None
    phone_number = None
    user_type = None
    created_at = None

    def __init__(self, phone_number, username, password, userType, createdAt):
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.user_type = userType
        self.created_at = createdAt

    def login(self, phone_number, password):
        return

    def get_name(self):
        return self.username

    def signup(self, phone_number, username, password, user_type):
        return

    def change_password(self, phone_number, password):
        self.password = password
        return None

    def logout(self):
        self.username = None
        self.phone_number = None
        self.password = None
        return

    def notification(self, phone_number, user_type):
        return None
