from __future__ import annotations
from datetime import datetime
import re


KEY = "Key TSTFEED0300|7E3E|0400"
SRC = "hblog.txt"
OUT = "hb_test.log"
TS_RE = re.compile(r"Timestamp (\d{2}:\d{2}:\d{2})")


def parse_ts(line: str) -> str | None:
    m = TS_RE.search(line)
    return m.group(1) if m else None


def sec_diff(prev_ts: str, next_ts: str) -> int:
    t1 = datetime.strptime(prev_ts, "%H:%M:%S")
    t2 = datetime.strptime(next_ts, "%H:%M:%S")
    diff = int((t1 - t2).total_seconds())
    if diff < 0:
        diff += 24 * 3600
    return diff


def analyze_hb(src_path: str = SRC, out_path: str = OUT) -> str:
    rows: list[tuple[str, str]] = []
    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if KEY in line:
                ts = parse_ts(line)
                if ts:
                    rows.append((ts, line.strip()))
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(f"HB анализ ключа: {KEY}\n")
        out.write("Уточнение: WARNING если 31 < heartbeat < 33; ERROR если heartbeat >= 33\n\n")
        for (ts1, _), (ts2, _) in zip(rows, rows[1:]):
            hb = sec_diff(ts1, ts2)
            if 31 < hb < 33:
                out.write(f"WARNING heartbeat = {hb}s at {ts1} (next={ts2})\n")
            elif hb >= 33:
                out.write(f"ERROR heartbeat = {hb}s at {ts1} (next={ts2})\n")
    return out_path


if __name__ == "__main__":
    path = analyze_hb()
    print(f"Done: {path}")