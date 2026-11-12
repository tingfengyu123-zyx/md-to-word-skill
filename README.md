# md-to-word

把 Markdown（含 LaTeX 公式）转成 Word 文档的 Agent Skill。公式转成 Word 原生公式，可以直接编辑，不是截图。

## 这是什么

一个按需加载的 Skill，给 AI Agent 用的"操作手册 + 工具脚本"。

按课上讲的拆法：

| 部分 | 对应内容 |
| --- | --- |
| SKILL.md | 说明书：什么时候用、按什么步骤做、有哪些坑 |
| convert.py | 工具：真正动手把 md 转成 docx 的脚本 |
| example.md | 示例输入，拿来测试和演示 |
| README.md | 给人看的说明 |

Agent 遇到"把 md 转成 Word"这类请求时，加载 SKILL.md，照着走一遍流程。

## 功能

- Markdown → Word `.docx`
- `$...$`、`$$...$$` 的 LaTeX 公式 → Word 原生公式（`<m:oMath>`）
- 正文统一设为宋体，页边距固定
- 转完报告"公式数 / 段落数"，用来核对公式有没有丢

## 环境

- pandoc 3.x：`%LOCALAPPDATA%\Programs\pandoc\pandoc.exe`
- Python 3 + python-docx

## 用法

```bash
python convert.py <输入.md> [输出.docx]
```

不写输出路径，就同名放在输入旁边。

## 示例

拿 `example.md` 试：

```bash
python convert.py example.md
```

得到 `example.docx`，里面的导数公式都是可编辑的原生公式。

## 已知限制

- 不支持自定义宏（`\bm` 这类）
- 精细排版（表格对齐、字号）要转完再单独调
- 老式 `.doc` 不能直接转，得先另存为 docx

## License

MIT
