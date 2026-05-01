class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connected = False
        return cls._instance

    def connect(self):
        self.connected = True
        return "Database connected to Repair System"

    def status(self):
        return "Connected" if self.connected else "Not Connected"
