from factories.RepositoryFactory import RepositoryFactory

class RepairJobService:

    def __init__(self):
        self.repo = RepositoryFactory.get_repair_job_repository("MEMORY")

    def create_job(self, job):
        self.repo.save(job)

    def get_job(self, job_id):
        return self.repo.find_by_id(job_id)

    def get_all_jobs(self):
        return self.repo.find_all()

    def delete_job(self, job_id):
        self.repo.delete(job_id)
