def merge_dicts(a, b):
    """
    ادغام دو دیکشنری؛ در صورت وجود کلید مشابه، مقدار دیکشنری b جایگزین می‌شود
    """
    result = a.copy()
    result.update(b)
    return result
