from junk_generator import junk_generator as generator
 
generator.generate(
    max_functions=5,
    gDocstring=True,
    gTypehint=True,
    gTypecheck=True,
    gPrint=False,
    gReturn=True,
    gFillLists=True,
    gFillDicts=True,
    gMaxListEntries=5,
    gMaxDictEntries=5,
    save_file="output.txt"
)