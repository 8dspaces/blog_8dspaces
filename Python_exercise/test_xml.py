# coding: utf8
#author: wklken
#desc: use to read db xml config.
#-----------------------
#2012-02-18 created
#----------------------

import sys,os
from xml.dom import minidom, Node

def read_dbconfig_xml(xml_file_path):
    content = {}

    root = minidom.parse(xml_file_path)
    table = root.getElementsByTagName("table")[0]

    #read dbname and table name.
    table_name = table.getAttribute("name")
    db_name = table.getAttribute("db_name")

    if len(table_name) > 0 and len(db_name) > 0:
        db_sql = "create database if not exists `" + db_name +"`; use " + db_name + ";"
        table_drop_sql = "drop " + table_name + " if exists " + table_name + ";"
        content.update({"db_sql" : db_sql})
        content.update({"table_sql" : table_drop_sql })
    else:
        print "Error:attribute is not define well!  db_name=" + db_name + " ;table_name=" + table_name
        sys.exit(1)
    #print table_name, db_name

    table_create_sql = "create table " + table_name +"("

    #read primary cell
    primary_key = table.getElementsByTagName("primary_key")[0]
    primary_key_name = primary_key.getElementsByTagName("name")[0].childNodes[0].nodeValue

    table_create_sql += primary_key_name + " INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,"

    #print primary_key.toxml()
    #read ordernary field
    fields = table.getElementsByTagName("field")
    f_index = 0
    for field in fields:
        f_index += 1
        name = field.getElementsByTagName("name")[0].childNodes[0].nodeValue
        type = field.getElementsByTagName("type")[0].childNodes[0].nodeValue
        table_create_sql += name + " " + type
        if f_index != len(fields):
            table_create_sql += ","
            is_index = field.getElementsByTagName("is_index")[0].childNodes[0].nodeValue

    table_create_sql += ");"
    content.update({"table_create_sql" : table_create_sql})
    #character set latin1 collate latin1_danish_ci;
    print content


if __name__ == "__main__":
    read_dbconfig_xml(r"D:\PythonExercise\table.xml")
    #read_dbconfig_xml(sys.argv[1])
