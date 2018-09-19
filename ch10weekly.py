
def get_country_codes(prices):
    import string
    result = ""
    for i in prices:
        if i in string.ascii_letters:
            result += i
        elif i == ',':
            result += ', '
    return(result)


def main():

    print(get_country_codes("NZ$300, KR$1200, DK$5"), "Answer:", "NZ, KR, DK")
    print(get_country_codes("US$40, AU$89, JP$200"), "Answer:", "US, AU, JP")
    print(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "Answer:", "AU, NG, MX, BG, ES")
    print(get_country_codes("CA$40"), "Answer:", "CA")



if __name__ == "__main__":
    main()
