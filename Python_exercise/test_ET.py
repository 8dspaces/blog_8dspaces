# coding: utf8

import xml.etree.ElementTree as ET 

xmldoc = """
<?xml version="1.0" encoding="UTF-8"?>
<table name="top_query" db_name="evaluting_sys">
<primary_key>
<name>id</name>
</primary_key>
<field>
<name>query</name>
<type>varchar(200)</type>
<is_index>false</is_index>
<description>query</description>
</field>
<field>
<name>pv</name>
<type>integer</type>
<is_index>false</is_index>
<description>pv</description>
</field>
<field>
<name>avg_money</name>
<type>integer</type>
<is_index>false</is_index>
<description></description>
</field>
</table>
"""
content = {}

# tree = ET.parse(xml_file_path)
# root = tree.getroot()
root = ET.fromstring(xmldoc.strip())
table = root.attrib

primary_key = root.find("primary_key").find("name").text

content.update(table)
content.update({root.find("primary_key").tag: primary_key})

fields = root.findall("field")
for field in fields:
    field_content = {}
    name = field.find("name")
    type = field.find("type")
    is_index = field.find("is_index")
    description = field.find("description")
    field_content.update({
                        type.tag: type.text,
                        is_index.tag: is_index.text,
                        description.tag: description.text
                        })
    content.update({name.text: field_content})
    
print content