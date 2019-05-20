import re
import pprint
import sys

class PathwayFile:
    """
    This class deals with data from the KEGG genes/pathway file.

    pathway file is a DBGET file containing all the pathway entries and its related data.
    """

    def __init__(self, reader):
        self.dbgetr = reader 
        self.pathway_entries = {}

    def generate_pathway_data( self ):
        """
        Generate a dictionary containing pathway file data.

        This method is selective, in other words, despite the 'pathway' file has a great amount of information,
        this method only append some specific (and most useful) data.

        But feel free to improve the result dictionary with more fields from the 'pathway' file.

        Returns:
            (dict): Pathway file data in a dictionary format.
        """

        pathway_entries = self.dbgetr.all_entries()

        re_pathway_internal_id = re.compile('^(T[0-9]{1,})\s(.*)$')

        for pathway_entry in pathway_entries:

            # NAME is a typical key in the 'pathway' file.
            # And Draft Genomes doesn't have a key NAME.
            # So, we're using 'NAME' as a criteria to tell if it's a valid pathway entry.
            if 'NAME' in pathway_entry:

                pathway_name = pathway_entry['NAME'][0]

                pathway_class = []
                if 'CLASS' in pathway_entry:
                    pathway_class = pathway_entry['CLASS']

                ko_pathway = []
                if 'KO_PATHWAY' in pathway_entry:
                    ko_pathway = pathway_entry['KO_PATHWAY']

                disease = []
                if 'DISEASE' in pathway_entry:
                    disease = pathway_entry['DISEASE']

                description = []
                if 'DESCRIPTION' in pathway_entry:
                    description = pathway_entry['DESCRIPTION']

                dblinks = []
                if 'DBLINKS' in pathway_entry:
                    dblinks = pathway_entry['DBLINKS']

                compound = []
                if 'COMPOUND' in pathway_entry:
                    compound = pathway_entry['COMPOUND']

                organism = []
                if 'ORGANISM' in pathway_entry:
                    organism = pathway_entry['ORGANISM']

                pathway_map = pathway_entry['PATHWAY_MAP'][0]
                pathway_map = pathway_map.split(' ')
                pathway_map = pathway_map[0]

                data = { 'pathway_map': pathway_map, 'name': pathway_name, 'pathway_class': pathway_class, 'disease': disease, 'ko_pathway': ko_pathway, 'dblinks': dblinks , 'compound': compound, 'organism': organism, 'description': description } 

                self.pathway_entries[pathway_map] = data 

        return self.pathway_entries 


    def load_pathway_data( self ):
        """
        Load the pathway file in case it wasn't already loaded.
        """

        if len( self.pathway_entries ) == 0:
            self.generate_pathway_data()


