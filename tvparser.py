# encoding: utf-8
#!/usr/bin/python
from xmlparser import XmlParser
import sys

if __name__ == "__main__":
    # Send country argument no XmlParser class    
    tvparser = XmlParser(sys.argv[1])
    tvparser.parse()
