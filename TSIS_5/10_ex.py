def is_lower(txt):
        import re
        s = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', txt)
        return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s).lower()

print(is_lower('PythonLanguage'))