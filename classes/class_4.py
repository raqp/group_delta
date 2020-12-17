class Car:
    mark = "BMV"

    def __init__(self, max_speed, color="Red"):
        self.color = color
        self.max_speed = max_speed

    def change_color(self, new_color):
        self.color = new_color


car_1 = Car(200)
car_2 = Car(150, "black")

car_1.change_color("white")
print(car_1.mark)
print(car_2.mark)
Car.mark = "BMW"
print()
print(car_1.mark)
print(car_2.mark)
