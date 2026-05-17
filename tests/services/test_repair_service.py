from services.repair_service import RepairService


def test_create_repair():

    service = RepairService()

    repair = {
        "repair_id": "R001",
        "device": "HP Laptop",
        "status": "Pending"
    }

    result = service.create_repair(repair)

    assert result["status"] == "Pending"
