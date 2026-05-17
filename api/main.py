from fastapi import FastAPI

from services.customer_service import CustomerService
from services.technician_service import TechnicianService
from services.repair_service import RepairService

app = FastAPI()

customer_service = CustomerService()
technician_service = TechnicianService()
repair_service = RepairService()


@app.get("/")
def home():
    return {"message": "Computer Repair Management System API"}


# ---------------- CUSTOMER ----------------

@app.post("/api/customer/create")
def create_customer(customer: dict):
    return customer_service.create_customer(customer)


@app.get("/api/customer/all")
def get_all_customers():
    return customer_service.get_all_customers()


@app.get("/api/customer/{customer_id}")
def get_customer(customer_id: str):
    return customer_service.get_customer(customer_id)


# ---------------- TECHNICIAN ----------------

@app.post("/api/technician/create")
def create_technician(technician: dict):
    return technician_service.create_technician(technician)


@app.get("/api/technician/all")
def get_all_technicians():
    return technician_service.get_all_technicians()


# ---------------- REPAIR JOB ----------------

@app.post("/api/repair/create")
def create_repair(repair: dict):
    return repair_service.create_repair(repair)


@app.get("/api/repair/all")
def get_all_repairs():
    return repair_service.get_all_repairs()


@app.post("/api/repair/{repair_id}/assign/{technician_id}")
def assign_technician(repair_id: str, technician_id: str):
    return repair_service.assign_technician(repair_id, technician_id)


@app.post("/api/repair/{repair_id}/complete")
def complete_repair(repair_id: str):
    return repair_service.complete_repair(repair_id)
