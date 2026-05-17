from services.technician_service import TechnicianService


def test_create_technician():

    service = TechnicianService()

    technician = {
        "technician_id": "T001",
        "name": "John",
        "specialization": "Laptop Repair"
    }

    result = service.create_technician(technician)

    assert result["specialization"] == "Laptop Repair"

