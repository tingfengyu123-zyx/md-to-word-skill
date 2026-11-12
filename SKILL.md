---
name: md-to-word
description: Convert a Markdown file (with LaTeX math) to a Word .docx with native equations and 宋体 body text; optionally export PDF. Use for 数学讲义、习题详解、翻译作业等 md → Word 的活.
---

# Markdown 转 Word（带原生公式）

把写好的 Markdown（含 `$...$`、`$$...$$` 的 LaTeX 公式）转成 Word 文档。
公式会变成 Word 原生公式（`<m:oMath>`），不是图片，能继续编辑。

## 什么时候用

- 用户说「做成 Word」「转 docx」「文档」且源文件是我写的 md
- 需要交电子稿，格式要求宋体、1.5 倍行距之类

## 步骤

1. 先写好 `.md`。行内公式用 `$...$`，独立公式用 `$$...$$`，两边留空行。
2. 跑本目录的 `convert.py`：

```
python convert.py <输入.md> [输出.docx]
```

不写输出路径，就同名放在输入旁边。

3. 转完会打印「公式数 N 段落 M」，用这个数字判断公式有没有转丢：
   md 里写了多少条公式，N 就该差不多；明显少就是 pandoc 没认出来。

## 环境

- pandoc 在 `%LOCALAPPDATA%\Programs\pandoc\pandoc.exe`（本机已装 3.13）
- python 用 `C:\Users\DELL PRO 14\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe`（带 python-docx）

## 转完必做

- 发给用户前，确认公式没丢、段落没乱。
- 默认只发微信、不放桌面；用户说放桌面才放。

## 附加

- `.doc`（老格式）不能直接转：先 Word COM 打开另存为 docx 再处理。
- 要 PDF：用 Word COM `SaveAs([ref]$pdf, [ref]17)`，或者调用 office-export-pdf 技能。

## 已知坑

- pandoc 不认识 `\operatorname` 以外的自定义宏，别用 `\bm` 这类。
- 中文输出到控制台是 GBK 乱码，但文件内容正确，别当故障。
- 表格对齐、字号这类精细要求，转完再用 python-docx 单独调。
