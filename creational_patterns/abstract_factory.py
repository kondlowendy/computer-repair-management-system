from abc import ABC, abstractmethod

# ===== Abstract Products =====

class DiagnosticTool(ABC):
    @abstractmethod
    def run_diagnostics(self):
        pass


class RepairTool(ABC):
    @abstractmethod
    def perform_repair(self):
        pass


# ===== Windows Products =====

class WindowsDiagnostic(DiagnosticTool):
    def run_diagnostics(self):
        return "Running Windows diagnostics"


class WindowsRepairTool(RepairTool):
    def perform_repair(self):
        return "Repairing system on Windows"


# ===== Mac Products =====

class MacDiagnostic(DiagnosticTool):
    def run_diagnostics(self):
        return "Running Mac diagnostics"


class MacRepairTool(RepairTool):
    def perform_repair(self):
        return "Repairing system on MacOS"


# ===== Abstract Factory =====

class RepairFactory(ABC):
    @abstractmethod
    def create_diagnostic(self):
        pass

    @abstractmethod
    def create_repair_tool(self):
        pass


# ===== Concrete Factories =====

class WindowsFactory(RepairFactory):
    def create_diagnostic(self):
        return WindowsDiagnostic()

    def create_repair_tool(self):
        return WindowsRepairTool()


class MacFactory(RepairFactory):
    def create_diagnostic(self):
        return MacDiagnostic()

    def create_repair_tool(self):
        return MacRepairTool()
