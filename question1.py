def convert_file_path(file_path: str) -> str:
    fps = file_path.split("/")
    result = []
    for fp in fps:
        if fp == ".":
            continue
        if fp == "..":
            result.pop()
            continue
        result.append(fp)
    return "/".join(result)
