
## Features

- 100% valid python syntax and code
- Generate ***int, bool, str, list, dict***
- Generate Docstring
- Generate Typehint
- Generate Typecheck
- Generate Prints
- Generate Return
## Usage/Examples

```python
from junk_generator import junk_generator as generator
 
generator.generate(max_functions=5)
```
| Parameter | Type  | Description|
| :-------- | :---- | :--------- |
| `max_functions` | `int` | the number of functions to generate |
| `gDocstring` | `bool` | if the function should include a docstring |
| `gTypehint` | `bool` | if the function should include type hinting |
| `gTypecheck` | `bool` | if the function should include type checking |
| `gPrint` | `bool` | if the function should include a print |
| `gReturn` | `bool` | if the function should have a return statement |
| `gFillLists` | `bool` | if the function should generate list data |
| `gFillDicts` | `bool` | if the function should generate dict data |
| `gMaxListEntries` | `int` | the amount of data to generate for lists |
| `gMaxDictEntries` | `int` | the amount of data to generate for dicts |
| `save_file` | `str` | the file to save the generated functions to |