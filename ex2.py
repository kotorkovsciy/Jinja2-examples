from jinja2 import Template

data = """{% raw %}Модуль Jinjia вместо
определения {{ name }}
подставляет соответствующее значение {% endraw %}"""

tm = Template(data)
msg = tm.render(name='Фёдор')

print(msg)