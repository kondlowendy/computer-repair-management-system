from creational_patterns.simple_factory.repair_factory import RepairFactory

def test_create_screen_repair():
    repair = RepairFactory.create_repair("screen", "iPhone cracked")
    assert repair.repair_type == "Screen Repair"
