#!/usr/bin/env python3

"""
Serialization and deserialization of XML files
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialization of XML file
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialization of XML file
    """
    data = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        data[child.tag] = child.text
    return data