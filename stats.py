def sort_on(items):
    return items["num"]

def no_of_words(text):
    all_words = text.split()
    return len(all_words)

def dict_word_count(text):
    final_dict = {} 
    lower_text = text.lower()
    for char in lower_text:
        if char in final_dict:
            final_dict[char] +=1
        else:
            final_dict[char] = 1
    return final_dict

def report_of_dict(dict):
    dicts_list = []
    for key in dict:
        new_dict = {}
        new_dict['char'] = key
        new_dict['num'] = dict[key]
        dicts_list.append(new_dict)
    dicts_list.sort(key=sort_on, reverse=True)
    return dicts_list
