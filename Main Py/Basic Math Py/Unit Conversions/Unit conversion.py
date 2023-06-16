class UnitConversion:
    def __init__(self):
        self.conversions = {
            "m": {"cm": 100, "mm": 1000, "in": 39.3701, "ft": 3.28084},
            "kg": {"g": 1000, "lb": 2.20462, "oz": 35.274},
            "s": {"ms": 1000, "us": 1000000, "ns": 1000000000}
        }

    def convert(self, value, unit_from, unit_to):
        try:
            return value * self.conversions[unit_from][unit_to]
        except Exception as e:
            print(f"Invalid unit(s) entered: {unit_from} -> {unit_to}")
            

# Create an instance of the UnitConversion class
obj = UnitConversion()

# Convert 200 cm to g
value = 200
unit_from = "m"
unit_to = "ft"
result = obj.convert(value, unit_from, unit_to)
print(f"{value} {unit_from} = {result} {unit_to}")
