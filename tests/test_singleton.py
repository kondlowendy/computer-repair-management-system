from creational_patterns.singleton import DatabaseConnection

def test_singleton_instance():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    assert db1 is db2  # same instance

def test_singleton_connection():
    db = DatabaseConnection()
    assert db.connect() == "Database connected to Repair System"
    assert db.status() == "Connected"
