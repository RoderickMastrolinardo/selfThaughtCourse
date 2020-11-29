import re

txt = "Arizona 479, 501, 870. California 209, 213, 650."

a = re.findall("\d+", txt)

print(a)
