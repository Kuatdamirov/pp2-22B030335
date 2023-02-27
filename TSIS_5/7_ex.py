def is_upper(txt):
        import re
        s = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', txt)
        return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s).upper()

print(is_upper('PythonLanguage'))