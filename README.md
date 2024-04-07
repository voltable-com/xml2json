# xml2json

This is a simple python script that converts XML to JSON. 
It is a command line tool that takes an XML file as input and outputs the JSON representation of the XML.

## Installation

This script requires Python 3.x or later.

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

Specifiy the input file and output file using the `-f` and `-o` flags respectively.

```bash
python xml2json.py -f input.xml -o output.json
```

If the output file is not specified, the JSON representation will be printed to the console.
```bash
python xml2json.py -f input.xml
```

## Executable
We could make the script executable using the following steps:

1. Add the following line to the top of the script:
```bash
pyinstaller --onefile xml2json.py
```

This will create an executable file in the `dist` directory.