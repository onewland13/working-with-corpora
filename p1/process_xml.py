import sys, os
import xml.etree.ElementTree
from bs4 import BeautifulSoup

from tei_reader import TeiReader
reader = TeiReader()

def getAbsPath(relPath): 
    curDir = os.getcwd()
    filePath = os.path.join(curDir, relPath)
    return filePath

def getCast(filePath):
    file = open(filePath).read()
    e = BeautifulSoup(file, 'lxml')
    cast = e.findAll("role", id=True)
    print(cast)
    c1 = cast[0]
    print(c1)
    print(dir(c1))
    characterId = c1["id"]
    print(characterId)
    linesForCastMember = e.findAll(who=characterId)
    print(linesForCastMember[0])


if __name__ == "__main__" :
    path = getAbsPath('/Users/dylanphelan/Documents/College/Grad/1-Sem/working-with-corpora/p1/works/shakes/tit.xml')
    getCast(path)

"""
Corpora:
========
corpora.all_parts  corpora.corpora    corpora.documents  corpora.parts      corpora.text       corpora.xml
corpora.attributes corpora.divisions  corpora.node       corpora.tag        corpora.tostring(

BS4 XML Tree: 
=============
['HTML_FORMATTERS', 'XML_FORMATTERS', '__bool__', '__call__', '__class__', '__contains__', '__copy__', '__delattr__', '__delitem__',
 '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__',
 '__weakref__', '_all_strings', '_attr_value_as_string', '_attribute_checker', '_find_all', '_find_one', '_formatter_for_name',
 '_is_xml', '_lastRecursiveChild', '_last_descendant', '_select_debug', '_selector_combinators', '_should_pretty_print', 
 '_tag_name_matches_and', 'append', 'attribselect_re', 'attrs', 'can_be_empty_element', 'childGenerator', 'children', 'clear', 
 'contents', 'decode', 'decode_contents', 'decompose', 'descendants', 'encode', 'encode_contents', 'extract', 'fetchNextSiblings', 
 'fetchParents', 'fetchPrevious', 'fetchPreviousSiblings', 'find', 'findAll', 'findAllNext', 'findAllPrevious', 'findChild', 
 'findChildren', 'findNext', 'findNextSibling', 'findNextSiblings', 'findParent', 'findParents', 'findPrevious', 
 'findPreviousSibling', 'findPreviousSiblings', 'find_all', 'find_all_next', 'find_all_previous', 'find_next', 'find_next_sibling', 
 'find_next_siblings', 'find_parent', 'find_parents', 'find_previous', 'find_previous_sibling', 'find_previous_siblings',
 'format_string', 'get', 'getText', 'get_attribute_list', 'get_text', 'has_attr', 'has_key', 'hidden', 'index', 'insert',
 'insert_after', 'insert_before', 'isSelfClosing', 'is_empty_element', 'known_xml', 'name', 'namespace', 'next', 'nextGenerator',
 'nextSibling', 'nextSiblingGenerator', 'next_element', 'next_elements', 'next_sibling', 'next_siblings', 'parent',
 'parentGenerator', 'parents', 'parserClass', 'parser_class', 'prefix', 'preserve_whitespace_tags', 'prettify', 'previous',
 'previousGenerator', 'previousSibling', 'previousSiblingGenerator', 'previous_element', 'previous_elements', 'previous_sibling', 
 'previous_siblings', 'quoted_colon', 'recursiveChildGenerator', 'renderContents', 'replaceWith', 'replaceWithChildren', 
 'replace_with', 'replace_with_children', 'select', 'select_one', 'setup', 'string', 'strings', 'stripped_strings', 'tag_name_re',
 'text', 'unwrap', 'wrap']

"""
