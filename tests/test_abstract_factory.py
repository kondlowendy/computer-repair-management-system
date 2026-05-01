from creational_patterns.abstract_factory import WindowsFactory, MacFactory

def test_windows_factory():
    factory = WindowsFactory()
    diag = factory.create_diagnostic()
    repair = factory.create_repair_tool()

    assert diag.run_diagnostics() == "Running Windows diagnostics"
    assert repair.perform_repair() == "Repairing system on Windows"


def test_mac_factory():
    factory = MacFactory()
    diag = factory.create_diagnostic()
    repair = factory.create_repair_tool()

    assert diag.run_diagnostics() == "Running Mac diagnostics"
    assert repair.perform_repair() == "Repairing system on MacOS"



