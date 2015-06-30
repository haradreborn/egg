import re


link = "<a href=\"/madoti\" title=\"ddd (Madoti) | madoti.livemaster.ru\">ddd (Madoti)</a>"
print link
data = re.compile(
    "^(<a href=\"/).*(\" title=\")(.*)(\|)(.*)(\">).*(</a>)").match(link).groups()[2][:-1]

print data
