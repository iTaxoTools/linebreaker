# DNAconvert tool
This program can convert between different linebreaks of different os files.


## Usage
    usage: replacer.py [-h] [--cmd] [f] [format] [-l]


    positional arguments:
      f                the input directory containing input files
      format           The desired linebreak os-specific format

    optional arguments:
      -h, --help            show this help message and exit
      --cmd                 activates the command-line interface
      -l L                  output log file


  To open it as GUI tool

  ```
  python linebreaker.py

  ```

### Batch processing

If `input file` is a zip file, all files will be unpacked and will be converted with new files (named with extensions) and will be outputted to the input file directory. All the original input files will be remained unchanged.


## Recognised line-endings

No need to provide input file line endings; program will detect it and will output a log file mentioning file names with their line break endings and name of corresponding outputted files.If the iput file has unix line ending and requested line-ending format is also unix; No new output file will be generated for that particular file, rest will be processed as usual.  

Files with any type of zip extension will be uncompressed automatically
