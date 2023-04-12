def simplifyPath(path: str) -> str:
    dirStack = []
    path = path.split("/")
    for i in path:
        if dirStack and i == "..":
            dirStack.pop()
        elif i not in [".", "", ".."]:
            dirStack.append(i)
    return "/" + "/".join(dirStack)

path = "/.../"
print(simplifyPath(path))