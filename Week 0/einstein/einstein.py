def main():
    mass = int(input("m: "))
    energy = mass_to_energy(mass)
    print("E:", energy)

def mass_to_energy(m):
    c = 300000000
    e = m * pow(c, 2)
    return e


main()