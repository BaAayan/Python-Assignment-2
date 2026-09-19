class Car:
    """Base class representing a general car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        """Return a formatted description of the car."""
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Car):
    """A car powered by a battery. Inherits from Car."""

    def __init__(self, make, model, year, battery_size,
                 charging_time_hours=None, range_km=None):
        super().__init__(make, model, year)      # reuse the Car constructor
        self.battery_size = battery_size         # capacity in kWh
        self.charging_time_hours = charging_time_hours
        self.range_km = range_km

    def get_description(self):
        """Override: extend the Car description with the battery size."""
        return f"{super().get_description()} - {self.battery_size} kWh battery"

    def get_battery_description(self):
        """Return a detailed description of the battery."""
        details = f"Battery size: {self.battery_size} kWh"
        if self.range_km is not None:
            details += f"; estimated range: {self.range_km} km per charge"
        if self.charging_time_hours is not None:
            details += f"; full charge time: {self.charging_time_hours} hours"
        return details + "."


# ---- Demonstration ----
petrol_car = Car("Toyota", "Corolla", 2020)
ev = ElectricCar("Nissan", "Leaf", 2023, battery_size=62,
                 charging_time_hours=7.5, range_km=385)

print(petrol_car.get_description())
print(ev.get_description())
print(ev.get_battery_description())