class RepairJob:
    def __init__(self, customer, device, issue):
        self.customer = customer
        self.device = device
        self.issue = issue


class RepairJobBuilder:
    def __init__(self):
        self.customer = None
        self.device = None
        self.issue = None

    def set_customer(self, customer):
        self.customer = customer
        return self

    def set_device(self, device):
        self.device = device
        return self

    def set_issue(self, issue):
        self.issue = issue
        return self

    def build(self):
        return RepairJob(self.customer, self.device, self.issue)
