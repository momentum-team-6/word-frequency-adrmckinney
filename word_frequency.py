



STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

punc_list = r'''!()-[]{};:'"\, <>./?@#$%^&*_~'''


def print_word_freq(file):
    counts_dict = {}
    
    opened_file = open(file, 'r')
    read_file = opened_file.read().lower()
    
    for elem in read_file:
        if elem in punc_list:
            read_file = read_file.replace(elem, " ")

    read_file = read_file.split()

    read_file_copy = read_file.copy()

    for word in read_file:
        if word in STOP_WORDS:
            read_file_copy.remove(word)
    
    read_file_copy.sort()

    for word in read_file_copy:
        counts_dict[word] = read_file_copy.count(word)
    
    
    # sorted_words = sorted(counts_dict.items(), key=lambda x:x[1], reverse=True)
    
    # print(counts_dict.items())

    # print(counts_dict.keys())
    # values_sorted = sorted(counts_dict.values(), key=None, reverse=True)
    # print(values_sorted)

    # for item in counts_dict:
    #     key = counts_dict.keys()
    #     value = counts_dict.values()
    #     print(f"{key} | {value}")
    

    # for item in counts_dict.items():
    #     print(item)
        

    # print(sorted_words)
    # print(f'{sorted_words[key]} | {sorted_words[key][value]}')
    
    
        



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

