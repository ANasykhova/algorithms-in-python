import pytest
from solution import HashTable


# Граничный - пустая таблица
def test_empty_table():
    ht = HashTable()
    assert len(ht) == 0
    with pytest.raises(KeyError):
        ht.get("x")
    with pytest.raises(KeyError):
        ht.delete("x")

# Базовые: put и get
def test_put_and_get():
    ht = HashTable()
    ht.put("a", 1)
    ht.put("b", 2)
    assert ht.get("a") == 1
    assert ht.get("b") == 2

# Обновление существующего ключа
def test_put_updates_existing_key():
    ht = HashTable()
    ht.put("x", 10)
    ht.put("x", 99)
    assert ht.get("x") == 99
    assert len(ht) == 1

# delete: ключ пропадает, len уменьшается
def test_delete():
    ht = HashTable()
    ht.put("a", 1)
    ht.put("b", 2)
    ht.delete("a")
    assert len(ht) == 1
    with pytest.raises(KeyError):
        ht.get("a")
    with pytest.raises(KeyError):
        ht.delete("a")

# __contains__ и __len__
def test_contains_and_len():
    ht = HashTable()
    ht.put("k", 42)
    assert "k" in ht
    assert "missing" not in ht
    assert len(ht) == 1

# Дандер-методы: [] как синтаксический сахар
def test_dunder_setitem_getitem_delitem():
    ht = HashTable()
    ht["x"] = 7
    assert ht["x"] == 7
    del ht["x"]
    with pytest.raises(KeyError):
        _ = ht["x"]

# Коллизии: маленькая таблица, все попадают в один h1
def test_collisions_small_table():
    ht = HashTable(initial_capacity=2, load_factor=0.99)
    ht.put("a", 1)
    ht.put("b", 2)
    ht.put("c", 3)
    assert ht.get("a") == 1
    assert ht.get("b") == 2
    assert ht.get("c") == 3

# Ресайз: все элементы на месте после расширения
def test_resize_preserves_all_elements():
    ht = HashTable(initial_capacity=4, load_factor=0.5)
    for i in range(20):
        ht.put(f"key{i}", i)
    for i in range(20):
        assert ht.get(f"key{i}") == i

# Tombstone: после удаления цепочка поиска не рвется
def test_delete_does_not_break_probe_chain():
    ht = HashTable(initial_capacity=4, load_factor=0.99)
    # кладем три ключа, которые могут занять одну цепочку
    ht.put("a", 1)
    ht.put("b", 2)
    ht.put("c", 3)
    ht.delete("a")          # DELETED в цепочке
    assert ht.get("b") == 2
    assert ht.get("c") == 3
    ht.put("d", 4)          # должен переиспользовать слот с DELETED
    assert ht.get("d") == 4

# Разные типы ключей
@pytest.mark.parametrize("key, value", [
    (42, "int key"),
    (3.14, "float key"),
    ((1, 2), "tuple key"),
])
def test_various_key_types(key, value):
    ht = HashTable()
    ht.put(key, value)
    assert ht.get(key) == value
