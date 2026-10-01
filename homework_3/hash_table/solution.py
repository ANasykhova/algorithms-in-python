"""
№ 3. Хеш-таблица
Реализация на основе открытой адресации с двойным хешированием

Решение:
1) _buckets - плоский список слотов: _EMPTY, _DELETED или (key, value)
2) двойное хеширование:
   h1(key) = hash(key) % capacity - основная позиция
   h2(key) = 2*(|hash(key)| % (capacity//2)) + 1 - шаг, всегда нечетный
   нечетный шаг взаимно прост с любой степенью двойки (capacity = 2^k),
   что гарантирует обход всех слотов
3) _probe возвращает (found, idx):
   идем по цепочке, пропускаем DELETED (но запоминаем первый),
   останавливаемся на EMPTY или совпавшем ключе
4) удаление: ставим DELETED (tombstone) - последующий поиск продолжается,
   но этот слот может быть переиспользован при вставке
5) _resize при load_factor >= threshold: перехешируем все живые слоты

Сложность:
O(1) амортизированно для put/get/delete - редкий resize за O(n)
O(n) по памяти - плоский массив capacity элементов

Визуализация (capacity=8):
put("a", 1): h1=3, слот 3 пуст           => buckets[3] = ("a", 1)
put("b", 2): h1=3, слот 3 занят ("a")
             h2=5, пробуем (3+5)%8=0     => buckets[0] = ("b", 2)
delete("a"): buckets[3] = DELETED
get("b"):    h1=3, слот 3 = DELETED (не стоп, запомнили)
             h2=5, пробуем (3+5)%8=0     => ("b", 2) найден => 2
put("c", 3): h1=3, слот 3 = DELETED      => buckets[3] = ("c", 3)  # переиспользован
"""

_EMPTY = object()
_DELETED = object()


class HashTable:
    def __init__(self, initial_capacity=8, load_factor=0.6):
        self._capacity = initial_capacity
        self._size = 0
        self._load_factor = load_factor
        self._buckets = [_EMPTY] * self._capacity

    def _h1(self, key):
        return hash(key) % self._capacity

    def _h2(self, key):
        # шаг всегда нечетный => взаимно прост с 2^k
        return 2 * (abs(hash(key)) % (self._capacity // 2)) + 1

    def _probe(self, key):
        """
        Возвращает (found, idx):
        found=True  => ключ в таблице, idx = его позиция
        found=False => ключа нет, idx = лучший слот для вставки
        """
        i = self._h1(key)
        step = self._h2(key)
        first_deleted = None

        for _ in range(self._capacity):
            slot = self._buckets[i]
            if slot is _EMPTY:
                return False, (first_deleted if first_deleted is not None else i)
            if slot is _DELETED:
                if first_deleted is None:
                    first_deleted = i
            elif slot[0] == key:
                return True, i
            i = (i + step) % self._capacity

        return False, (first_deleted if first_deleted is not None else i)

    def put(self, key, value):
        if self._size / self._capacity >= self._load_factor:
            self._resize()

        found, idx = self._probe(key)
        if found:
            self._buckets[idx] = (key, value)
        else:
            self._buckets[idx] = (key, value)
            self._size += 1

    def get(self, key):
        found, idx = self._probe(key)
        if found:
            return self._buckets[idx][1]
        raise KeyError(key)

    def delete(self, key):
        found, idx = self._probe(key)
        if not found:
            raise KeyError(key)
        self._buckets[idx] = _DELETED
        self._size -= 1

    def _resize(self):
        old = self._buckets
        self._capacity *= 2
        self._size = 0
        self._buckets = [_EMPTY] * self._capacity
        for slot in old:
            if slot is not _EMPTY and slot is not _DELETED:
                self.put(slot[0], slot[1])

    def __len__(self):
        return self._size

    def __contains__(self, key):
        found, _ = self._probe(key)
        return found

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.delete(key)

    def __str__(self):
        pairs = []
        for slot in self._buckets:
            if slot is not _EMPTY and slot is not _DELETED:
                pairs.append(f"{slot[0]!r}: {slot[1]!r}")
        return "{" + ", ".join(pairs) + "}"

    def __repr__(self):
        return f"HashTable({str(self)})"


if __name__ == "__main__":
    ht = HashTable()
    ht.put("name", "Alice")
    ht.put("age", 30)
    print(ht)
    print("name:", ht.get("name"))
    ht.delete("age")
    print("after delete age:", ht)
    print("len:", len(ht))
    print("'name' in ht:", "name" in ht)
