from creational_patterns.simple_factory import DeviceFactory

def test_device_factory():
    laptop = DeviceFactory.create_device("laptop")
    assert laptop.get_type() == "Laptop"
