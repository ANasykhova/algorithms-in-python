import pytest
from solution import group_anagrams


def normalize(groups):
    # Сортируем группы внутри и между собой для стабильного сравнения
    return sorted(sorted(g) for g in groups)

# Граничный - пустой список и один элемент
@pytest.mark.parametrize("strs, answer", [
    ([], []),
    (["a"], [["a"]]),
    (["abc"], [["abc"]]),
])
def test_edge_cases(strs, answer):
    assert normalize(group_anagrams(strs)) == normalize(answer)

# Краевые - однобуквенные слова, дубликаты
@pytest.mark.parametrize("strs, answer", [
    (["a", "b", "a"], [["a", "a"], ["b"]]),
    (["ab", "ba", "cd", "dc", "ef"], [["ab", "ba"], ["cd", "dc"], ["ef"]]),
    (["listen", "silent", "enlist", "hello"], [["listen", "silent", "enlist"], ["hello"]]),
])
def test_nontrivial(strs, answer):
    assert normalize(group_anagrams(strs)) == normalize(answer)

# Базовые: нет анаграмм, все анаграммы друг друга
@pytest.mark.parametrize("strs, answer", [
    (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
    (["abc", "bca", "cab"], [["abc", "bca", "cab"]]),
    (["eat", "tea", "tan", "ate", "nat", "bat"], [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
])
def test_no_anagrams_and_all_anagrams(strs, answer):
    assert normalize(group_anagrams(strs)) == normalize(answer)
