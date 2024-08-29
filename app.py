import sqlite3

con = sqlite3.connect("cars.db")
cur = con.cursor()

def initTable():
    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        color,
        brand
    );""")

def addInitialData():
    cars = [
        ("blue", "mazda"),
        ("green", "honda"),
        ("brown", "mercedes"),
        ("black", "mazda")
    ]
    cur.executemany("INSERT INTO cars (color, brand) VALUES (?, ?)", cars)
    con.commit()



def addCar():
    brand = input("which brand you wish to add? ")
    color = input("which color is the car you wish to add? ")
    cur.execute(f"INSERT INTO cars (brand, color) VALUES ('{brand}', '{color}')")
    con.commit()

def exitApp(): exit()

def showCars():
    for car in cur.execute('select * from cars'):
        print(car)

def searchByBrand():
    carToSearch = input("which car type you want to find? ")
    for car in cur.execute(f"select * from cars WHERE brand = '{carToSearch}'"):
        print(car) 

def menu():
    print("add a car - 1")
    print("search a car by brand - 2")
    print("show all cars - 3")
    print("exit - 4")

    choice = input("state your choice, mate: ")

    if(choice == '1'): addCar()
    elif(choice == '2'): searchByBrand()
    elif(choice == '3'): showCars()
    elif(choice == '4'): exitApp()


def main():
    initTable()
    addInitialData()
    while True:
        menu()

if __name__ == "__main__":
    main()