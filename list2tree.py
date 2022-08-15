import json


parts_layers = [
    {"id": 1, "name": "部门1", "pid": 0},
    {"id": 2, "name": "部门2", "pid": 1},
    {"id": 5, "name": "部门5", "pid": 4},
    {"id": 4, "name": "部门4", "pid": 3},
    {"id": 3, "name": "部门3", "pid": 1},
    {"id": 6, "name": "部门3", "pid": 3},
]


def list_to_tree(parts: list[dict]) -> dict:
    """ 将一个层级结构转换成一个树状结构，根据pid和id的关系进行转换。

    :param parts: 扁平化的部门列表
    :return: 转换成树状结构的部门列表

    """
    if not parts:
        return {}
    # 先排个序，方便操作
    parts = sorted(parts, key=lambda x: x["id"])
    # 获取跟节点
    root = parts[0]
    for part in parts[1:]:
        pid = part.get("pid")
        """:type:int"""
        if parts[pid-1].get("children"):
            parts[pid-1]["children"].append(part)
        else:
            parts[pid-1]["children"] = [part]
    return root


def list_to_tree2(parts: list[dict]) -> dict:
    """ 将一个层级结构转换成一个树状结构，根据pid和id的关系进行转换。如果id不连续，则这么处理。

    :param parts: 扁平化的部门列表
    :return: 转换成树状结构的部门列表

    """
    if not parts:
        return {}
    # 先排个序，方便操作
    parts = sorted(parts, key=lambda x: x["id"])
    # 获取跟节点
    root = parts[0]
    for part in parts[1:]:
        pid = part.get("pid")
        """:type:int"""
        for p in parts:
            if p.get("id") != pid:
                continue
            if not p.get("children"):
                p["children"] = [part]
            else:
                p["children"].append(part)
            break
    return root


if __name__ == '__main__':
    result = list_to_tree2(parts_layers)
    result_json = json.dumps(result, ensure_ascii=False, indent=4, separators=(',', ': '))
    print(result_json)


