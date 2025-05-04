def test(func, expected_output, *args):
    from copy import deepcopy
    safe_args = [deepcopy(arg) if isinstance(arg, list) else arg for arg in args]
    actual = func(*safe_args)
    assert actual == expected_output, (
        f"\n Test failed:\n"
        f"Function: {func.__name__}\n"
        f"Input:    {args}\n"
        f"Returned: {actual}\n"
        f"Expected: {expected_output}\n"
    )
    print(f" {func.__name__}{args} => {actual}")