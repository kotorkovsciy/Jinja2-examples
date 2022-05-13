from jinja2 import Template

persons = [
    {"name" : "Алексей", "old" : 18, "weight" : 78.5},
    {"name" : "Николай", "old" : 28, "weight" : 82.3},
    {"name" : "Иван", "old" : 33, "weight" : 94.0}
]

tpl = """
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
"""

tm = Template(tpl)
msg = tm.render(users = persons)

print(msg)