from creational_patterns.builder import RepairJobBuilder

def test_builder():
    job = (RepairJobBuilder()
           .set_customer("John")
           .set_device("Laptop")
           .set_issue("Screen broken")
           .build())

    assert job.customer == "John"
    assert job.device == "Laptop"
