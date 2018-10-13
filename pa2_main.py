if __name__ == "__main__":

    my_list = ["calvin", "and", "hobbes", "are", "the", "first", "spaceman", "on", "mars"]

    # Joins list and capitalizes the first letter of each word.
    def cap_join(my_list):
        new_string = " ".join(my_list).title()
        return new_string

    # Prints capitalized list as string.
    print(cap_join(my_list))

