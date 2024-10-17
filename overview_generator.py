from os import scandir
from re import sub
from sys import argv

docs_folder = "docs" if len(argv) <= 1 else argv[1]
output_file = "test_overview.md" if len(argv) <= 2 else argv[2]

# 自动替换设置（正则表达式）
replacement = {
  r"\[地图下载站\]": r"[地图下载站](#ballance-地图下载站)",
  r"\((\.\/)?(.+)\.md\)": lambda match: f"(#{match.group(2).lower().replace(' ', '-')})"
}

# 头部信息
header_text = ""
with open("README.md") as f:
  for line in f:
    if line.startswith("## "):  # 仅保留 README 中一级标题与描述
      break
    header_text += line

# 整理 Mod 信息
docs = []
for item in scandir(docs_folder):
  if item.is_file() and item.name.endswith(".md"):
    mod_name = item.name[:-3]  # 文件名作为 Mod 名称
    overview = ""
    content = ""
    with open(item.path, "r") as f:
      mod_desc_flag = True
      for line in f:
        if line.startswith("#"):
          line = "##" + line  # 标题级别 +2
        content += line
        if line.startswith("### "):
          overview += f"- [{mod_name}](#{mod_name.lower().replace(' ', '-')}): "
          content += "\n[<small>**返回 Mod 列表**</small>](#mod-列表)\n"
        elif mod_desc_flag and (desc := line.strip()) and not desc.startswith("#### 基础信息") and not desc.startswith("**"):
          overview += desc + "\n"
          mod_desc_flag = False
    for k, v in replacement.items():
      content = sub(k, v, content)  # 正则替换
    doc = {
      'name': mod_name,
      'overview': overview,
      'content': content,
    }
    docs.append(doc)

# Mod 文档内容
content_text = ""
overview_text = f"""## Mod 获取方式

### Ballance 地图下载站

绝大多数 Mod 均可以在 [Ballance 地图下载站](http://ballancemaps.ysepan.com)下载（虽然名称是 “地图” 下载站，但实际上也可以下载到 Mod）。

### 其他下载方式

- 有些 Mod 因为需要时常更新，或者内容不太适合正常发布，地图下载站不会收录。请参见 Mod 具体介绍内列出的下载方式。
- 很多 Mod 也可以从各常用 Ballance 交流群的群文件内下载。
- 有能力者自然可以直接从 Mod 源码自行编译。

## Mod 列表

本文档已收录共 **{len(docs)}** 个 Mod。以下列表仅为各 Mod 的简要介绍。**详细信息（包括下载地址等）请查看各 Mod 名称上的链接所指向的位置**。

"""
docs = sorted(docs, key = lambda x: "" if x['name'] == "BallanceModLoader" else x['name'])
for doc in docs:
  overview_text += doc['overview']
  content_text += "\n" + doc['content']

with open(output_file, "w") as f:
  f.write(header_text)
  f.write(overview_text)
  f.write("\n## Mod 详解\n")
  f.write(content_text)
