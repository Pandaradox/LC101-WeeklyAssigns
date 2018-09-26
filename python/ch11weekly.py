def sort_contacts(contacts):
    names = list(contacts.keys())
    done = 0
    while True:
        for i in range(len(names)-1):
            if names[i] > names[i+1]:
                (names[i], names[i+1]) = (names[i+1], names[i])
                done = 1
        if done == 0:
            break
        else:
            done = 0
    results = []
    for i in names:
        results.append((i, contacts[i][0], contacts[i][1]))
    return(results)


def main():

    set1 = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
    "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
    "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}

    print(sort_contacts(set1))

    # [('Freud, Anna', '1-541-754-3010',
    # 'anna@psychoanalysis.com'), ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
    # ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')])

    print("\n", sort_contacts({"Summitt, Pat": ("1-865-355-4320", "pat@greatcoaches.com"),
    "Rudolph, Wilma": ("1-410-5313-584", "wilma@olympians.com")}),

    [('Rudolph, Wilma', '1-410-5313-584', 'wilma@olympians.com'),
    ('Summitt, Pat', '1-865-355-4320', 'pat@greatcoaches.com')])

    print("\n", sort_contacts({"Dinesen, Isak": ("1-718-939-2548", "isak@storytellers.com")}),
    [('Dinesen, Isak', '1-718-939-2548', 'isak@storytellers.com')])

    print("\n", sort_contacts({"Rimbaud, Arthur": ("1-636-555-5555", "arthur@notlive.com"),
    "Swinton, Tilda": ("1-917-222-2222", "tilda@greatActors.com"),
    "Almodovar, Pedro": ("1-990-622-3892", "pedro@filmbuffs.com"), "Kandinsky, Wassily":
    ("1-333-555-9999", "kandinsky@painters.com")}),

    [('Almodovar, Pedro', '1-990-622-3892',
    'pedro@filmbuffs.com'), ('Kandinsky, Wassily', '1-333-555-9999', 'kandinsky@painters.com'),
    ('Rimbaud, Arthur', '1-636-555-5555', 'arthur@notlive.com'), ('Swinton, Tilda',
    '1-917-222-2222', 'tilda@greatActors.com')])


if __name__ == "__main__":
    main()
