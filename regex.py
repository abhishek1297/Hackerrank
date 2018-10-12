import re
regex_pattern = r"[,.]"
print '\n'.join(re.split(regex_pattern, "String, is, Separated, By, Commas.T.N.T."))