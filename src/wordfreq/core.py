"""词频统计的核心逻辑。"""

import re
from collections import Counter
from typing import Iterable, List, Optional, Tuple

# 英文单词或连续中文字符
_TOKEN_RE = re.compile(r"[a-zA-Z]+|[\u4e00-\u9fff]+")


def tokenize(text: str) -> List[str]:
    """将文本切分为词元:英文按单词、中文按连续汉字切分,统一转为小写。

    Args:
        text: 输入文本。

    Returns:
        词元列表。
    """
    return [m.group(0).lower() for m in _TOKEN_RE.finditer(text)]


def count_words(
    text: str,
    stopwords: Optional[Iterable[str]] = None,
    top_n: Optional[int] = None,
    sort_by: str = "count",
) -> List[Tuple[str, int]]:
    """统计文本中词元出现的频率。

    Args:
        text: 输入文本。
        stopwords: 需要排除的词元集合(可选)。
        top_n: 只返回前 N 个结果(可选)。
        sort_by: 排序方式,"count" 按词频降序,"alpha" 按字母序。

    Returns:
        (词元, 次数) 元组列表。

    Raises:
        ValueError: 当 sort_by 不是 "count" 或 "alpha" 时。
    """
    if sort_by not in ("count", "alpha"):
        raise ValueError("sort_by 必须是 'count' 或 'alpha'")

    stop = {w.lower() for w in stopwords} if stopwords else set()
    tokens = [t for t in tokenize(text) if t not in stop]
    counter = Counter(tokens)

    if sort_by == "alpha":
        items = sorted(counter.items(), key=lambda kv: kv[0])
    else:
        items = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))

    return items[:top_n] if top_n is not None else items
