from sys import argv

input_file = "README.md" if len(argv) <= 1 else argv[1]
output_file = "test_overview.md" if len(argv) <= 2 else argv[2]

header_text = ""
overview_text = ""
content_text = ""
with open(input_file, "r") as f:
  mod_flag = False
  mod_desc_flag = False
  for line in f:
    if mod_flag:
      content_text += line
      if line.startswith("### "):
        mod_name = line.strip()[4:]
        overview_text += f"- [{mod_name}](#{mod_name.lower().replace(' ', '-')}): "
        content_text += "\n[<small>**返回 Mod 列表**</small>](#mod-列表)\n"
        mod_desc_flag = True
      elif mod_desc_flag and (desc := line.strip()) and not desc.startswith("#### 基础信息") and not desc.startswith("**"):
        overview_text += desc + "\n"
        mod_desc_flag = False
    else:
      if line.startswith("## Mod 详解"):
        content_text += line
        mod_flag = True
        overview_text += "## Mod 列表\n\n本列表仅为各 Mod 的简要介绍。**详细信息（包括下载地址等）请查看各 Mod 名称上的链接所指向的位置**。\n\n"
      else:
        header_text += line

with open(output_file, "w") as f:
  f.write(header_text)
  f.write(overview_text)
  f.write("\n")
  f.write(content_text)
