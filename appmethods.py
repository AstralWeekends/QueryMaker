# Formats list of Doc IDs like sqlizer:
def formatcopy(inputlist: 'str') -> str:
    listified = inputlist.split(sep = '\n')
    list_nospace = [i for i in listified if i != '']
    listresult = ("('" + "','".join(list_nospace) + "')")
    return listresult

def makequery(source, min_source, max_dest, docids_in) -> str:
    docids = formatcopy(docids_in)
    id_offset = (int(max_dest) - int(min_source)) + 1
    query = f"SELECT ~IsActive AS Deleted, ID + {id_offset} AS Id2, * FROM {source} WHERE DocID IN {docids}"
    return(query)