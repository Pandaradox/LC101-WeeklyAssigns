# ########################################


class Car():
    def __init__(self, gas_level):
        self.gas_level = float(gas_level)
        print("Vroom Vroom!")

    def add_fuel(self, amount):
        return(13-self.gas_level)

    def fill_up(self):
        if self.gas_level < 13:
            return(13.0 - self.gas_level)
        else:
            return(0)


def main():


    # some tests to check your code, Do Not Post These in Vocareum
    print( Car(10).fill_up(), 3 )
    print( Car(20).fill_up(), 0 )
    print( Car(5.5).fill_up(), 7.5 )
    print( Car(12.5).fill_up(), 0.5 )
    print( Car(13).fill_up(), 0 )
    civic = Car(12.0)
    civic.__init__(13.0)


if __name__ == "__main__":
    main()
