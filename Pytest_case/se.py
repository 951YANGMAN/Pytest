from typing import Any



def apply_slice(data: list[Any], s: slice) -> list[Any]:
    return data[s]

# 合法调用：
apply_slice([0, 1, 2, 3, 4], slice(1, 4))  # 返回 [1, 2, 3]
# apply_slice([0, 1, 2, 3, 4], slice(None, None, 2))  # 返回 [0, 2, 4]
