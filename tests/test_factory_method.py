from creational_patterns.factory_method import RepairFactory

def test_hardware():
    factory = RepairFactory()
    repair = factory.create_repair("hardware")
    assert repair.process() == "Processing hardware repair"

def test_software():
    factory = RepairFactory()
    repair = factory.create_repair("software")
    assert repair.process() == "Processing software repair"
