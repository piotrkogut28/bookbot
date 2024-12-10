def on_sort(dict):
    return dict["char"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    text_low = file_contents.lower()
    words = file_contents.split()
  
    print(len(words))
    dict1 = {}
    for char in text_low:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1  
    sorted_dict = dict(sorted(dict1.items(),key=lambda item:item[1] ,reverse=False))
    print(sorted_dict)
    for char in dict1:
        print(f"The '{char}' was found {dict1[char]} times!")

if __name__ == '__main__':
    main()

