from abc import ABC, abstractmethod

# Product
class RepairProcessor(ABC):
    @abstractmethod
    def process(self):
        pass

# Concrete Products
class HardwareRepair(RepairProcessor):
    def process(self):
        return "Processing hardware repair"

class SoftwareRepair(RepairProcessor):
    def process(self):
        return "Processing software repair"

# Factory
class RepairFactory:
    def create_repair(self, repair_type):
        if repair_type == "hardware":
            return HardwareRepair()
        elif repair_type == "software":
            return SoftwareRepair()
        else:
            raise ValueError("Unknown repair type")
