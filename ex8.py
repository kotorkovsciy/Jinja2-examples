from jinja2 import Template

html = """
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
"""

tm = Template(html)
msg = tm.render()

print(msg)