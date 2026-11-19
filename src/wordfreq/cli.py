"""命令行入口。"""

import argparse
import sys
from typing import List, Optional

from .core import count_words


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wordfreq",
        description="统计文本文件中的词频(支持中英文混合)。",
    )
    parser.add_argument("file", help="要统计的文本文件路径,使用 - 表示标准输入")
    parser.add_argument("-n", "--top", type=int, default=10, help="输出前 N 个结果(默认 10)")
    parser.add_argument(
        "--sort",
        choices=["count", "alpha"],
        default="count",
        help="排序方式:count 按词频降序,alpha 按字母序(默认 count)",
    )
    parser.add_argument("--stopwords", help="停用词文件路径(每行一个词)")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    if args.file == "-":
        text = sys.stdin.read()
    else:
        try:
            with open(args.file, encoding="utf-8") as f:
                text = f.read()
        except OSError as e:
            print(f"错误:无法读取文件 {args.file}: {e}", file=sys.stderr)
            return 1

    stopwords = None
    if args.stopwords:
        try:
            with open(args.stopwords, encoding="utf-8") as f:
                stopwords = [line.strip() for line in f if line.strip()]
        except OSError as e:
            print(f"错误:无法读取停用词文件 {args.stopwords}: {e}", file=sys.stderr)
            return 1

    results = count_words(text, stopwords=stopwords, top_n=args.top, sort_by=args.sort)
    for word, count in results:
        print(f"{word}\t{count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
