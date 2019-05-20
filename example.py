# -*- coding: utf-8 -*-

import pprint

# Import essential modules
from dbgetreader import * 
from pathwayfile.pathwayfile import *

# Load the reader and load the dbgetreader
dbget = DBGET(file_to_read='./tests/fixtures/pathway')
dbgetr = DBGETReader(reader=dbget)

pathway_file = PathwayFile(reader=dbgetr)

pathway_file.generate_pathway_data()

data = pathway_file.pathway_entries

pprint.pprint(data)
