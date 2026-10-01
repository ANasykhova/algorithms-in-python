"""
№ 2. Anagrams
Сгруппировать слова-анаграммы из списка

Решение:
1) для каждого слова строим ключ = tuple(sorted(word))
   анаграммы имеют одинаковый набор букв => одинаковый ключ
2) добавляем слово в словарь по этому ключу
3) возвращаем значения словаря - готовые группы

Сложность:
O(n * L * log L) по времени - для каждого из n слов сортируем L символов
O(n * L) по памяти - словарь хранит все слова

Визуализация:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

"eat" => sorted => "aet" => groups = {"aet": ["eat"]}
"tea" => sorted => "aet" => groups = {"aet": ["eat","tea"]}
"tan" => sorted => "ant" => groups = {"aet": [...], "ant": ["tan"]}
"ate" => sorted => "aet" => groups = {"aet": ["eat","tea","ate"], "ant": ["tan"]}
"nat" => sorted => "ant" => groups = {"aet": [...], "ant": ["tan","nat"]}
"bat" => sorted => "abt" => groups = {"aet": [...], "ant": [...], "abt": ["bat"]}

Ответ: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
"""


def group_anagrams(strs: list) -> list:
    groups = {}
    for word in strs:
        key = tuple(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


if __name__ == "__main__":
    strs = input("words: ").split()
    for group in group_anagrams(strs):
        print(group)
