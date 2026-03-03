import json
import glob

# 获取当前目录下所有 .md 文件
md_files = glob.glob("chapter*.md")
md_files.sort()  # 按文件名排序

print(f"找到以下文件: {md_files}")

for md_file in md_files:
    # 生成对应的 json 文件名（chapter1.md -> chapter1.json）
    json_file = md_file.replace(".md", ".json")
    
    result = []
    current_chapter = None
    current_section = None

    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        # 一级标题（会）
        if line.startswith("### "):
            current_chapter = {
                "title": line.replace("### ", "").strip(),
                "sections": []
            }
            result.append(current_chapter)

        # 二级标题
        elif line.startswith("#### "):
            current_section = {
                "title": line.replace("#### ", "").strip(),
                "chants": []
            }
            current_chapter["sections"].append(current_section)

        # 咒句
        elif line.startswith(">##### "):
            chant_text = line.replace(">##### ", "").strip()
            current_section["chants"].append({
                "text": chant_text,
                "pinyin": "",
                "meaning": ""
            })

        # 拼音
        elif line.startswith(">>     "):
            pinyin = line.replace(">>     ", "").strip()
            current_section["chants"][-1]["pinyin"] = pinyin

        # 释义
        elif line.startswith(">>>     "):
            meaning = line.replace(">>>     ", "").strip()
            current_section["chants"][-1]["meaning"] = meaning

    # 保存为对应名称的 json 文件
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✓ {md_file} -> {json_file}")

print("\n全部转换完成！")