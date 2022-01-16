# dicrea
A dictionary creator collecting words from files or web pages on a specific sector (e.g. banking sector) based on a specific pattern. Pattern is defined via regexs' inside python source file. Planning to add this as an optional argument.

Input is usually a web page or file containing terms and glossary of a specific sector. Using regexps and \<p><b\> as statring delimiters every term is extracted and stored in an output file
```console
python3 dicrea.py -h
usage: dicrea.py [-h] [-f FILE] [-u URL] [-o OUTPUT] [-a APPEND]

This is a dictionary creator

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file
  -u URL, --url URL     Input url
  -o OUTPUT, --output OUTPUT
                        Output file
  -a APPEND, --append APPEND
                        Append to output file
```
![alt text](shot1.png)

![alt text](shot2.png)
