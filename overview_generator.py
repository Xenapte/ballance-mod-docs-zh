from sys import argv

if len(argv) < 3:
  print("Usage: python overview_generator.py <input markdown> <output markdown> <output link>")
  exit()

input_file = argv[1]
output_file = argv[2]
output_link = argv[3]

output_text = ""
with open(input_file, "r") as f:
  mod_flag = False
  mod_desc_flag = False
  for line in f:
    if mod_flag:
      if line.startswith("### "):
        mod_name = line.strip()[4:]
        output_text += f"* [{mod_name}]({output_link}#{mod_name.lower().replace(' ', '-')}): "
        mod_desc_flag = True
      elif mod_desc_flag and (desc := line.strip()) and not desc.startswith("#### 基础信息") and not desc.startswith("**"):
        output_text += desc + "\n"
        mod_desc_flag = False
    else:
      output_text += line
      if line.startswith("## Mod 列表"):
        mod_flag = True
        output_text += "\n本列表仅为各 Mod 的简要介绍。**详细信息请查看各 Mod 名称上的链接所指向的页面**。\n\n"

with open(output_file, "w") as f:
  f.write(output_text)
