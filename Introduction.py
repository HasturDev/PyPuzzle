

def Introduction(example):
    """Make an entry into the dictionary. When this entry is called the dictionary will print
    an explination of your puzzle. Make sure to include the call required to run your test."""

    dictionary = {'example':'Text', 'first_test':'Simply import the test file with from tests import first_test'}
    
    if example == "list":
        print(" here are the puzzles you have now:" + ' ' + str(list(dictionary.keys())))
    elif example == "help":
        print("""First call Introduction(list) that will help you find the name of the challenge.\n
         Once you have found the name just call Introduction(name) to get that challenges description.\n
         The description should inform you of what test to import in order to complete the challenge.\n
         Once that's done just upload your completion to github and link it in the discord.\n
         """)
    else:
        print(dictionary[example])
