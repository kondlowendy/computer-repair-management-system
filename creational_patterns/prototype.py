import copy

# ===== Prototype =====

class RepairTemplate:
    def __init__(self, device_type, issue, estimated_cost):
        self.device_type = device_type
        self.issue = issue
        self.estimated_cost = estimated_cost

    def clone(self):
        return copy.deepcopy(self)

    def summary(self):
        return f"{self.device_type} - {self.issue} - R{self.estimated_cost}"


# ===== Prototype Registry (Cache) =====

class RepairTemplateCache:
    def __init__(self):
        self._cache = {}

    def load_defaults(self):
        self._cache["laptop_screen"] = RepairTemplate("Laptop", "Screen Replacement", 1500)
        self._cache["phone_battery"] = RepairTemplate("Phone", "Battery Replacement", 800)
        self._cache["desktop_os"] = RepairTemplate("Desktop", "OS Repair", 1200)

    def get(self, key):
        return self._cache[key].clone()
