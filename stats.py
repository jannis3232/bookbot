def count_words(content):         
    words = content.split()
    return len(words)

def count_characters(content):
    lower_content = content.lower()
    dir = {}
    for character in lower_content:
        dir[character] = dir.get(character, 0) + 1
    return dir    

def sort_on(items):
    return items["num"]

def sort_dict(dictonary):
    sorted_list = []
    for k in dictonary:
        sorted_list.append({"char": k, "num": dictonary[k]})
    sorted_list.sort(reverse=True, key = sort_on)
    return sorted_list    

def print_header(path, num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

def print_foot():
    print("============= END ===============")        