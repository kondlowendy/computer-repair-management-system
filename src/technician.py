class Technician:
    def __init__(self, tech_id, name, specialization):
        self.tech_id = tech_id
        self.name = name
        self.specialization = specialization

    def assign_job(self, job):
        job.technician = self
