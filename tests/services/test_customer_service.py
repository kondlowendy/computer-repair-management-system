from services.customer_service import CustomerService


def test_create_customer():

    service = CustomerService()

    customer = {
        "customer_id": "C001",
        "name": "Wendy",
        "email": "wendy@gmail.com"
    }

    result = service.create_customer(customer)

    assert result["name"] == "Wendy"
