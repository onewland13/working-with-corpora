import sys, os
import re
from bs4 import BeautifulSoup
import json
import pickle
import nltk
from nltk.tokenize import RegexpTokenizer

def getAllWorks(pathToWorks):
    """
        Returns: 
            an array of paths to all works we care about
    """
    print("Getting all our works ")
    curDir = os.getcwd()
    directory = os.path.join(curDir, pathToWorks)
    return [
        os.path.join(directory, work)
        for work in os.listdir(directory) 
        if os.path.isfile(os.path.join(directory, work))
    ]

def getXMLTree(filePath): 
    """
        Given an path to an XML file, builds a navigable tree of that file using BS4 
    """
    print("Building an XML tree for the work")
    print(filePath)
    file = open(filePath).read()
    xmlTree = BeautifulSoup(file, 'lxml')
    return xmlTree

def processLines(blocksOfSpeech): 
    """
        Process blocks of speech into the different lines a character speaks
        sanitizing the words in a few different ways: 
            1. Lowercase all the words 
            2. Remove puncutation
            3. Remove all stage directions and any words that may follow them.
            4. Remove extraneous whitespace characters, like newlines and tabs
            5. Remove exits, which come in the form of "Exit." and "Exuent."; we'll 
               drop following words here similarly to the stage directions 
            6. 
    """
    processedLines = []
    for block in blocksOfSpeech: 
        textOfBlock = block.findAll("l")
        for lineElement in textOfBlock:
            # Remove extraneous whitespace
            line = lineElement.text
            line = line.replace('\n', " ")
            line = line.replace('\t', " ")
            # Lowercase all words: 
            lProcessed = line.lower()
            # Remove punctuation and extra spaces
            tokenizer = RegexpTokenizer(r'\w+')
            lProcessed = ' '.join(tokenizer.tokenize(lProcessed))
            # Remove Stage directions
            lProcessed = re.sub(r'\[.*', '', lProcessed)
            # Remove exits
            lProcessed = re.sub(r'Exit|Exuent.*', '', lProcessed)
            if (lProcessed != ""): 
                processedLines.append(lProcessed)
    return processedLines 

def getLinesForCast(xmlTree):
    print("Getting script for Tree")
    cast = xmlTree.findAll("role", id=True)
    # Create a dictionary 
    linesByCastMember = {}
    for character in cast:
        characterName = character.text 
        characterId = character["id"]
        linesForCastMember = xmlTree.findAll(who=characterId)
        # linesObject = {}
        # Process lines before storing
        processedLines = processLines(linesForCastMember)
        # Store data on object
        # linesObject["name"] = characterName
        # linesObject["lines"] = processedLines
        if(len(processedLines) != 0): 
            linesByCastMember[characterName] = processedLines
    return linesByCastMember

def writeScriptToJSON(script, srcFile):
    print("Jsonifying: ", workName)
    fileHandler = open(f"./json/{srcFile}.json", 'w')
    json.dump(script, fileHandler)
    fileHandler.close()  

def writeEncodingGenderDoc(characters, srcFile):
    print("Creating lookup for srcFile: ", srcFile)
    # For GODS sake don't overwrite
    if (os.path.isfile(f"./genders/{srcFile}.json")): 
        print(f"FAILED - We already have a file for {srcFile}")
        return
    fileHandler = open(f"./genders/{srcFile}-genders.json", 'w')
    genderLookup = {}
    for char in characters: 
        # Default to male to save time
        genderLookup[char] = "M"
    json.dump(genderLookup, fileHandler)
    fileHandler.close()  


if __name__ == "__main__" :
    path = sys.argv[1] 
    if not path: 
        path = f'works'
    works = getAllWorks(path)
    for workPath in works:
        workName = os.path.basename(workPath)
        print(workName)
        tree = getXMLTree(workPath)
        scriptByCharacter = getLinesForCast(tree)
        # Create files for
        writeEncodingGenderDoc(scriptByCharacter, workName)
        writeScriptToJSON(scriptByCharacter, workName) 
    
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
