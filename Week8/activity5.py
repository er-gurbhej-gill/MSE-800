class travel_package:

    def __init__(self):
        self.destination = None
        self.hotel = None
        self.transport = None
        self.meal_plan = None
        self.activities = None
        self.insurance = None

    def display_package(self):
        print("destination:", self.destination)
        print("hotel:", self.hotel)
        print("transport:", self.transport)
        print("meal_plan:", self.meal_plan)
        print("activities:", self.activities)
        print("insurance:", self.insurance)


class travel_package_builder:

    def __init__(self):
        self.package = travel_package()

    def set_destination(self, destination):
        self.package.destination = destination
        return self

    def set_hotel(self, hotel):
        self.package.hotel = hotel
        return self

    def set_transport(self, transport):
        self.package.transport = transport
        return self

    def set_meal_plan(self, meal_plan):
        self.package.meal_plan = meal_plan
        return self

    def set_activities(self, activities):
        self.package.activities = activities
        return self

    def set_insurance(self, insurance):
        self.package.insurance = insurance
        return self

    def build(self):
        return self.package

builder = travel_package_builder()

package = (
    builder
    .set_destination("auckland")
    .set_hotel("5_star")
    .set_transport("flight")
    .set_meal_plan("breakfast")
    .set_activities("city_tour")
    .set_insurance("yes")
    .build()
)

package.display_package()