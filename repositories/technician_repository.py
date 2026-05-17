class TechnicianRepository:

    def __init__(self):
        self.technicians = []

    def create(self, technician):
        self.technicians.append(technician)
        return technician

    def get_all(self):
        return self.technicians

    def read(self, technician_id):
        for technician in self.technicians:
            if technician["technician_id"] == technician_id:
                return technician
        return None
