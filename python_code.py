class PowerSystemFault:
    def __init__(self, base_voltage_kv, base_power_mva):
        # Base values
        self.base_voltage = base_voltage_kv  # in kV
        self.base_power = base_power_mva  # in MVA
        self.base_impedance = (self.base_voltage ** 2) / self.base_power  # Zbase = Vbase^2 / Sbase
    
    def per_unit_impedance(self, actual_impedance):
        # Convert actual impedance to per-unit
        return actual_impedance / self.base_impedance
    
    def short_circuit_fault(self, pre_fault_voltage_pu, fault_impedance_pu):
        # Fault current calculation (I_f = V_pre / Z_f)
        fault_current_pu = pre_fault_voltage_pu / fault_impedance_pu
        print(f"Short-circuit fault: Fault Current (pu) = {fault_current_pu}")
        return fault_current_pu
    
    def open_circuit_fault(self, pre_fault_voltage_pu):
        # For an open circuit, current becomes zero, voltage is unchanged (assumed balanced condition)
        fault_current_pu = 0
        print(f"Open-circuit fault: Fault Current (pu) = {fault_current_pu}")
        return fault_current_pu

# Test harness to collect inputs from command line
def main():
    # User inputs
    base_voltage = float(input("Enter base voltage (kV): "))
    base_power = float(input("Enter base power (MVA): "))
    
    # Create the system
    system = PowerSystemFault(base_voltage, base_power)
    
    # Choose fault type
    fault_type = input("Enter fault type (short-circuit/open-circuit): ").strip().lower()
    pre_fault_voltage_pu = float(input("Enter pre-fault voltage (pu): "))
    
    if fault_type == "short-circuit":
        actual_impedance = float(input("Enter actual fault impedance (ohms): "))
        fault_impedance_pu = system.per_unit_impedance(actual_impedance)
        system.short_circuit_fault(pre_fault_voltage_pu, fault_impedance_pu)
    
    elif fault_type == "open-circuit":
        system.open_circuit_fault(pre_fault_voltage_pu)
    
    else:
        print("Invalid fault type entered.")

if __name__ == "__main__":
    main()
