
import xml.etree.ElementTree as ET
import os

def get_data(xml_file):
    file_path = os.path.join(os.getcwd(), xml_file)
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    items = root.findall('channel/item')
    return items

def get_short_list(items):
    total_list = []
    for item in items:
        a = item.find('description').text.lower()
        b = a.split(' ')
        total_list.extend(b)
    short = list(filter(lambda x: len(x) >= 6, total_list))
    return short

def count_words(some_list):
    dict_val = {}
    for word in some_list:
        if word in dict_val.keys():
            dict_val[word] += 1
        else:
            dict_val.setdefault(word, 1)

    return dict_val

def show_top_10(some_dict):
    p = sorted(some_dict, key=some_dict.get, reverse=True)
    for i in range(10):
        print(f'{p[i]}: {some_dict[p[i]]}')

items = get_data('newsafr.xml')
short_list = get_short_list(items)
dict_val = count_words(short_list)
show_top_10(dict_val)
