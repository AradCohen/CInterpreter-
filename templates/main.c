#include<stdio.h>
{% for include in includes %}
{{ include }}
{% endfor %}

int main()
{
    {% for line in user_code_lines %}
    {{ line }}
    {% endfor %}
    return 0;
}