from collections import Counter

def word(text):
    # Phân tách văn bản thành các từ
    words = text.split()
    
    # Xây dựng từ điển đếm số lần xuất hiện của mỗi từ
    word_freq = Counter(words)
    
    # Sắp xếp từ điển theo thứ tự giảm dần của số lần xuất hiện
    wordsort = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    
    # In ra số lần xuất hiện của các từ
    print("Số lần xuất hiện của các từ:")
    for word, freq in wordsort.items():
        print(f"{word}: {freq}")
# Nhập đoạn văn bản từ người dùng
text_input = input("Nhập một đoạn văn bản: ")
word(text_input)