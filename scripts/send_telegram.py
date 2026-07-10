#!/usr/bin/env python3
"""把当日 AI 热点日报推送到 Telegram。零依赖（纯标准库）。

配置: 工作区根目录 telegram配置.json（已 gitignore，绝不能提交）:
    {"bot_token": "123456:ABC-...", "chat_id": "123456789 或 @频道名"}

用法:
    python3 scripts/send_telegram.py               # 发送今日日报
    python3 scripts/send_telegram.py --date 2026-07-10
    python3 scripts/send_telegram.py --dry-run     # 只打印不发送

发送内容: ①标题 + 今日焦点板块(转 HTML,截断至 4096 内) ②完整日报 .md 作为文件附件。
"""

import argparse
import html as html_mod
import json
import re
import sys
import urllib.parse
import urllib.request
import uuid
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

WORKDIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = WORKDIR / "telegram配置.json"


def api_call(token, method, data=None, file_field=None, file_path=None):
    url = f"https://api.telegram.org/bot{token}/{method}"
    if file_path is None:
        body = urllib.parse.urlencode(data).encode()
        req = urllib.request.Request(url, data=body)
    else:  # multipart/form-data 手工拼装(stdlib 无现成封装)
        boundary = uuid.uuid4().hex
        parts = []
        for k, v in (data or {}).items():
            parts.append(f"--{boundary}\r\nContent-Disposition: form-data; "
                         f"name=\"{k}\"\r\n\r\n{v}\r\n".encode())
        parts.append(f"--{boundary}\r\nContent-Disposition: form-data; "
                     f"name=\"{file_field}\"; filename=\"{file_path.name}\"\r\n"
                     f"Content-Type: text/markdown\r\n\r\n".encode())
        parts.append(file_path.read_bytes())
        parts.append(f"\r\n--{boundary}--\r\n".encode())
        req = urllib.request.Request(url, data=b"".join(parts), headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            out = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        # Telegram 的 4xx 响应体里有具体原因(description)，必须读出来否则没法排障
        try:
            detail = json.loads(e.read().decode()).get("description", "")
        except Exception:
            detail = ""
        raise RuntimeError(f"Telegram API {e.code}: {detail or e.reason}") from None
    if not out.get("ok"):
        raise RuntimeError(f"Telegram API 错误: {out}")
    return out


def md_to_tg_html(text):
    """把日报的 markdown 片段转成 Telegram HTML(只处理用到的语法)。"""
    text = html_mod.escape(text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"^#{1,3} (.+)$", r"<b>\1</b>", text, flags=re.M)
    return text


def extract_focus(report_text):
    """抽出标题行 + 今日焦点板块。"""
    title = report_text.strip().splitlines()[0].lstrip("# ").strip()
    m = re.search(r"## 🔥 今日焦点\n(.*?)(?=\n## )", report_text, re.S)
    focus = m.group(1).strip() if m else "(未找到焦点板块)"
    return title, focus


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="YYYY-MM-DD,默认今天(Asia/Shanghai)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not CONFIG_PATH.exists():
        print(f"SKIP: 未配置 Telegram({CONFIG_PATH.name} 不存在),跳过推送")
        sys.exit(0)  # 未配置不算失败,方便流水线里无条件调用
    cfg = json.loads(CONFIG_PATH.read_text("utf-8"))
    token, chat_id = cfg["bot_token"], cfg["chat_id"]
    if "在这里" in str(token) or not token:
        print("SKIP: telegram配置.json 里还是占位符,跳过推送")
        sys.exit(0)

    date = args.date or datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")
    report = WORKDIR / "待审核" / date / "AI热点日报.md"
    if not report.exists():
        print(f"FAIL: 日报不存在: {report}")
        sys.exit(1)

    title, focus = extract_focus(report.read_text("utf-8"))
    msg = f"<b>{html_mod.escape(title)}</b>\n\n<b>🔥 今日焦点</b>\n{md_to_tg_html(focus)}"
    if len(msg) > 4000:  # Telegram 单条上限 4096
        msg = msg[:4000] + "\n…(焦点过长已截断,全文见附件)"

    if args.dry_run:
        print(f"[dry-run] 将发送到 chat_id={chat_id}:\n{msg[:500]}...\n[dry-run] 附件: {report}")
        return

    api_call(token, "sendMessage", {
        "chat_id": chat_id, "text": msg, "parse_mode": "HTML",
        "disable_web_page_preview": "true"})
    api_call(token, "sendDocument", {"chat_id": chat_id,
             "caption": f"AI 热点日报 · {date} 全文"},
             file_field="document", file_path=report)
    print(f"OK: 已推送到 Telegram(焦点消息 + 全文附件) chat_id={chat_id}")


if __name__ == "__main__":
    main()
