def get_num_words(text):
    return len(text.split())

def get_num_chars(text):

    dict = {}

    for char in text:
        char = char.lower()
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1
    return dict

def sorted_list(dict):

    def sort_on(dict):
        return dict["num"]
    
    list = []
    for key, value in dict.items():
        list.append({ 
            "char": key,
            "num": value
        })
    list.sort(reverse=True, key=sort_on)

    return list
