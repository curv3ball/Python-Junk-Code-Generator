import random, string

class junk_generator:
    """useless ass python junk code generator"""
    result = "" # will update periodically

    def random_type() -> str:
        """returns a random index from a hardcoded list of types"""
        types = ["int","bool", "str", "list", "dict"]
        return random.choice(types)

    def random_text(chatacterLimit: int = 20) -> str:
        """returns a random string with a specified character limit"""
        characters = string.ascii_letters + string.digits
        random_string = random.choice(string.ascii_letters)

        for _ in range(chatacterLimit - 1):
            random_string += random.choice(characters)

        return random_string

    def random_sentence(sentence_length: int = 10) -> str:
        """returns a random sentence made from lorem ipsum words"""

        # a big piece of lorem ipsum split up by each word, a better alternative to this is to put it in a text file and parse the file at runtime
        words_list = [ "Lorem", "ipsum", "dolor", "sit", "amet,", "consectetur", "adipiscing", "elit.", "Sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua."]
        sentence = ' '.join(random.choice(words_list) for _ in range(sentence_length))
        sentence = sentence.capitalize() + '.'
        return sentence

    def random_number(min = 10000, max = 10000000) -> int:
        """returns a random int between a specified minimum and maximum"""
        return ( random.randint(min, max) )

    def generate(
            max_functions: int = 5, 
            gDocstring: bool = True,
            gTypehint: bool = True,
            gTypecheck: bool = True,
            gPrint: bool = True,
            gReturn: bool = True,
            gFillLists: bool = True,
            gFillDicts: bool = True,
            gMaxListEntries: int = 5,
            gMaxDictEntries: int = 5,
            save_file: str ="output.txt"
            ) -> str:
        """generates a python junk code function\n
        gDocstring      -> if the function should include a docstring\n
        gTypehint       -> if the function should include type hinting\n
        gTypecheck      -> if the function should include type checking\n
        gPrint          -> if the function should print out the variable name\n
        gReturn         -> if the function should return the variable\n
        gFillLists      -> if the function should generate random data for any lists that get generated\n
        gFillDicts      -> if the function should generate random data for any dictionaries that get generated\n
        gMaxListEntries -> the maximum amount of random data to generate for a function if gFillLists is enabled\n
        gMaxDictEntries -> the maximum amount of random data to generate for a function if gFillDicts is enabled\n
        save_file       -> the destination for the save file
        """
        result = ""

        for i in range(max_functions):
            _type = junk_generator.random_type()
            _function = junk_generator.random_text()
            _variable = junk_generator.random_text()
            _value = None
            
            # typehint
            if gTypehint:
                result += f"def {_function}() -> {_type}:\n    "
            else:
                result += f"def {_function}():\n    "

            # docstring
            if gDocstring:
                result += f'"""{junk_generator.random_sentence()}"""\n    '
            
            # body
            if _type == "int":
                _value = f'{junk_generator.random_number()} {random.choice(["+", "-", "*", "/", "^"])} {junk_generator.random_number()}'
            elif _type == "bool":
                _value = "True" if junk_generator.random_number(0, 1) == 1 else "False"
            elif _type == "str":
                _value = f'"{junk_generator.random_text()}"'
            elif _type == "list":
                _value = "[]"
                if gFillLists:
                    _value = "["
                    for i in range(gMaxListEntries):
                        gen = junk_generator.random_number(0, 2)
                        if gen == 0: gen = junk_generator.random_number()
                        elif gen == 1: gen = "True" if junk_generator.random_number(0, 1) == 1 else "False"
                        elif gen == 2: gen = f'"{junk_generator.random_text()}"'
                        _value += f"{gen}"
                        if i < gMaxListEntries - 1:
                            _value += ","
                    _value += "]"
            elif _type == "dict":
                _value = "{}"
                if gFillDicts:
                    _value = "{"
                    for i in range(gMaxDictEntries):
                        dictIndex = junk_generator.random_text()
                        gen = junk_generator.random_number(0, 2)
                        if gen == 0: gen = junk_generator.random_number()
                        elif gen == 1: gen = "True" if junk_generator.random_number(0, 1) == 1 else "False"
                        elif gen == 2: gen = f'"{junk_generator.random_text()}"'
                        _value += f'"{dictIndex}" : {gen}'
                        if i < gMaxDictEntries - 1:
                            _value += ","
                    _value += "}"

            # typehint
            if gTypehint:
                result += f"{_variable}: {_type} = {_value}\n"
            else:
                result += f"{_variable} = {_value}\n"

            # typecheck
            if gTypecheck:
                result += f"    if type({_variable}) is {_type}:\n        {_variable} = {_variable}\n"

            # print
            if gPrint:
                result += f"    print({_variable})\n"

            # return
            if gReturn:
                result += f"    return ({_type}({_variable}))"

            result += "\n\n"

        with open(save_file, "w") as file:
            file.write(result)
        print(result)
