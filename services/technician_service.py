from repositories.technician_repository import TechnicianRepository


class TechnicianService:

    def __init__(self):
        self.repository = TechnicianRepository()

    def create_technician(self, technician):

        if not technician.get("specialization"):
            raise ValueError("Specialization is required")

        return self.repository.create(technician)

    def get_all_technicians(self):
        return self.repository.get_all()

    def get_technician(self, technician_id):
        return self.repository.read(technician_id)
