# winsyspath

Definitive Python wrapper for Windows System Path

## Compatibility

-   Python 2.7.x
-   Python 3.x and newer

## Example

    import winsyspath

    # Directory to add in the System Path
    path = 'C:\\'

    # Init System Path wrapper and read its actual value
    syspath_wrapper = winsyspath.WinSysPath()

    # Try to add a path into System path
    try:
        if syspath_wrapper.add(path):
            print("The path "{}" is correctly added to the System Path".format(path))
        else:
            print("The path "{}" is already in System Path, so cannot be added".format(path))
    except (EnvironmentError, WindowsError, OSError, ValueError) as ex:
        print("Error -> {}".format(str(ex)))

    # Reload System path value (needed only if it is modified outside python)
    syspath_wrapper.reload()

    # Print System Path value as a list
    print(syspath_wrapper.get())

    # Print System Path value as a string
    print(syspath_wrapper.get_str())

    # Try to remove a path from System path
    try:
        if syspath_wrapper.remove(path):
            print("The path "{}" is correctly removed from System Path".format(path))
        else:
            print("The path "{}" is not in System Path, so cannot be removed".format(path))
    except (EnvironmentError, WindowsError, OSError, ValueError) as ex:
        print("Error -> {}".format(str(ex)))

## Sources

- <https://docs.python.org/2/library/_winreg.html>
- <https://docs.python.org/3/library/winreg.html>
