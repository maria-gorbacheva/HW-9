
import json
import os


def get_data(json_file):
    file_path = os.path.join(os.getcwd(), json_file)
    with open(file_path, encoding='utf-8') as f:
        json_data = json.load(f)
    descriptions = json_data['rss']['channel']['items']
    return descriptions


def words_list(root_list):
    """
    Generates list of each word (>=6 letters) found in all news. Each letter is in lowercase.
    :param root_list: list of dictionaries with the key "description" is required
    :return: list of words, each more than 6 letters
    """
    total_list = []
    for news in root_list:
        a = news['description'].lower()
        b = a.split(' ')
        total_list.extend(b)
        short = list(filter(lambda x: len(x) >= 6, total_list))
    return short


def count_words(some_list):
    """
    Generates a dictionary with words as keys and its frequencies of occurrence
    :param some_list: list of strings
    :return: dictionary
    """
    dict_val = {}
    for word in some_list:
        if word in dict_val.keys():
            dict_val[word] += 1
        else:
            dict_val.setdefault(word, 1)
    return dict_val


def show_top_10(some_dict):
    """
    Shows top-10 the most frequent words and their frequencies.
    :param some_dict: a dictionary
    :return: None
    """
    p = sorted(some_dict, key=some_dict.get, reverse=True)
    for i in range(10):
        print(f'{p[i]}: {some_dict[p[i]]}')

descriptions = get_data('newsafr.json')
all_news = words_list(descriptions)
dict_val = count_words(all_news)
show_top_10(dict_val)
