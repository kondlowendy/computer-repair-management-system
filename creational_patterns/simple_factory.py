class Laptop:
    def get_type(self):
        return "Laptop"


class Phone:
    def get_type(self):
        return "Phone"


class Desktop:
    def get_type(self):
        return "Desktop"


class DeviceFactory:
    @staticmethod
    def create_device(device_type):
        if device_type.lower() == "laptop":
            return Laptop()
        elif device_type.lower() == "phone":
            return Phone()
        elif device_type.lower() == "desktop":
            return Desktop()
        else:
            raise ValueError("Unknown device type")
