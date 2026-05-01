from abc import ABC, abstractmethod

# Product
class RepairService(ABC):
    @abstractmethod
    def execute(self):
        pass


class ScreenRepair(RepairService):
    def execute(self):
        return "Screen repair completed"


class BatteryRepair(RepairService):
    def execute(self):
        return "Battery replacement completed"


class SoftwareFix(RepairService):
    def execute(self):
        return "Software issue resolved"


# Factory
class RepairFactory:
    def create_repair(self, repair_type):
        if repair_type == "screen":
            return ScreenRepair()
        elif repair_type == "battery":
            return BatteryRepair()
        elif repair_type == "software":
            return SoftwareFix()
        else:
            raise ValueError("Unknown repair type")
