if __name__ == "__main__":

    my_list = ["calvin", "and", "hobbes", "are", "the", "first", "spaceman", "on", "mars"]

    # Joins list and capitalizes the first letter of each word.
    def cap_join(my_list):
        new_string = " ".join(my_list).title()
        return new_string

    # Prints capitalized string.
    print(cap_join(my_list))

    # In case a loop was wanted instead of the title method.

    # def cap_join(my_list):
    #     new_string = " ".join([my_list[word].capitalize() for word in range(len(my_list))])
    #     return new_string

