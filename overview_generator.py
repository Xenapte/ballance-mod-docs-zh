from os import scandir
from re import sub
from sys import argv

docs_folder = "docs" if len(argv) <= 1 else argv[1]
output_file = "test_overview.md" if len(argv) <= 2 else argv[2]

# 自动替换设置（正则表达式）
replacement = {
  r"\{地图下载站\}": r"[地图下载站](#ballance-地图下载站)",
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

with open("overview_header.md") as f:
  overview_text = f.read().replace("{len(docs)}", str(len(docs)))
  overview_text = overview_text[overview_text.find("\n## "):].strip() + "\n\n"

docs = sorted(docs, key = lambda x: "" if x['name'] == "BallanceModLoader" else x['name'])
for doc in docs:
  overview_text += doc['overview']
  content_text += "\n" + doc['content']

with open(output_file, "w") as f:
  f.write(header_text)
  f.write(overview_text)
  f.write("\n## Mod 详解\n")
  f.write(content_text)
