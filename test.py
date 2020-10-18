import re

end = "7-5"
p = re.compile("\d+$")
end = p.search(str(end))
print(end.group())
