import ast
import sys

def merge(translations_module_path, target_path="blog_content.py"):
    ns = {}
    with open(translations_module_path, encoding="utf-8") as f:
        exec(f.read(), ns)
    translations = ns["TRANSLATIONS"]

    with open(target_path, encoding="utf-8") as f:
        src = f.read()
    lines = src.split("\n")

    tree = ast.parse(src)
    assign = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "BLOG_ARTICLES" for t in node.targets
        ):
            assign = node
            break
    if assign is None:
        raise RuntimeError("BLOG_ARTICLES assignment not found")

    articles_dict = assign.value
    insertions = []
    missing = []
    already = []

    for key_node, val_node in zip(articles_dict.keys, articles_dict.values):
        bid = key_node.value
        if bid not in translations:
            continue
        existing_langs = {k.value for k in val_node.keys if isinstance(k, ast.Constant)}
        fr_value_node = None
        for k, v in zip(val_node.keys, val_node.values):
            if isinstance(k, ast.Constant) and k.value == "fr":
                fr_value_node = v
                break
        if fr_value_node is None:
            missing.append(bid)
            continue
        skip_langs = [lg for lg in ("de", "it", "en") if lg in existing_langs]
        if skip_langs:
            already.append((bid, skip_langs))
        insertions.append((fr_value_node.end_lineno, bid))

    for bid in translations:
        found = any(b == bid for _, b in insertions) or bid in missing
        if not found:
            missing.append(bid)

    if missing:
        print("MISSING (bid not found in BLOG_ARTICLES or no fr entry):", missing)
        sys.exit(1)

    insertions.sort(key=lambda x: -x[0])

    for end_lineno, bid in insertions:
        blocks = translations[bid]
        new_text = "\n".join(blocks[lg] for lg in ("de", "it", "en") if lg in blocks)
        lines.insert(end_lineno, new_text)

    new_src = "\n".join(lines)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(new_src)
    print(f"Merged {len(insertions)} articles' translations.")

if __name__ == "__main__":
    merge(sys.argv[1])
