# Lomuto partition (in-place)

from typing import List

def partition_lomuto(a: List[int], lo: int, hi: int) -> int:
    pivot = a[hi]                 # pivot лежит в конце
    i = lo                        # граница области < pivot

    for j in range(lo, hi):       # j сканирует всё, кроме pivot
        if a[j] < pivot:          # строго < (про равные ниже)
            a[i], a[j] = a[j], a[i]
            i += 1

    # ставим pivot на его финальную позицию i
    a[i], a[hi] = a[hi], a[i]
    return i
