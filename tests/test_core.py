"""核心函数的单元测试。"""

import pytest

from wordfreq import count_words, tokenize


def test_tokenize_english():
    assert tokenize("Hello world") == ["hello", "world"]


def test_tokenize_chinese():
    assert tokenize("你好世界,你好") == ["你好世界", "你好"]


def test_tokenize_mixed():
    assert tokenize("Hello 你好 hello") == ["hello", "你好", "hello"]


def test_count_words_basic():
    result = count_words("hello world hello python world")
    assert result == [("hello", 2), ("world", 2), ("python", 1)]


def test_count_words_top_n():
    result = count_words("a a a b b c", top_n=2)
    assert result == [("a", 3), ("b", 2)]


def test_count_words_stopwords():
    result = count_words("the quick brown fox", stopwords=["the"])
    assert "the" not in [w for w, _ in result]


def test_count_words_sort_alpha():
    result = count_words("banana apple cherry", sort_by="alpha")
    assert [w for w, _ in result] == ["apple", "banana", "cherry"]


def test_count_words_invalid_sort():
    with pytest.raises(ValueError):
        count_words("hello", sort_by="invalid")


def test_count_words_empty():
    assert count_words("") == []
