{% include 'header.htm' %}
{% block content %}
        {% block table_contents %}
        <ul>
            {% for li in list_table -%}
            <li>{% block item scoped %}{{ li }}{% endblock %}</li>
            {% endfor -%}
        </ul>
        {% endblock table_contents %}
{% endblock content %}
{% include 'footer.htm' %}