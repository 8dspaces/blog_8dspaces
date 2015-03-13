import csv 
import argparse

def csv2xml(csv_file, xml_file):

    reader = csv.reader(open(csv_file))
    xmlfile = open(xml_file, 'w')

    xmlfile.write('<?xml version="1.0"?>' + "\n")
    # there must be only one top-level tag
    xmlfile.write('<csv_data>' + "\n")

    row_num = 0
    for row in reader:
        if row_num == 0:
            tags = row
            for i in range(len(tags)):
                tags[i] = tags[i].replace(" ", "_")
        else:
            xmlfile.write('<row>' + '\n')
            for i in range(len(tags)):
                xmlfile.write('    ' + '<' + tags[i] + '>' + row[i] \
                            + '</' + tags[i] + '>' + '\n'
                )
            xmlfile.write('</row>' + '\n' )
        row_num = row_num + 1
        
    xmlfile.write('</csv_data>' + '\n')
    xmlfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='covert csv to xml file')
    
    parser.add_argument('--csv', help=r'Specify csv file')
    parser.add_argument('--xml', default='xml_out.xml', help=r'Specify xml file name')
    
    args = parser.parse_args()
    
    csv2xml(args.csv, args.xml)
        
    
    
    
    
