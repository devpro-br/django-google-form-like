from django.shortcuts import render
from django.utils.safestring import mark_safe


# Create your views here.

class FieldType:
    def __init__(self, label, html_type, html_name, required=True):
        self.required = required
        self.html_name = html_name
        self.html_type = html_type
        self.label = label

    def as_html(self, value=None):
        required_html_str= 'required="required"' if self.required else ''
        return f"""
        {self.label}: <br />
        <input type="{self.html_type}" name="{self.html_name}" {required_html_str} />
       """

class FieldValue:
    def __init__(self, field_type: FieldType, value:dict):
        self.value = value


class Template:
    def __init__(self):
        self.field_type_list: list[FieldType] = []

    def as_html(self):
        field_inputs_html_str = ''
        for field_type in self.field_type_list:
            field_inputs_html_str += field_type.as_html()
            field_inputs_html_str += '<br /><br />'

        return mark_safe(f"""
<form method="post">
    {field_inputs_html_str}
</form>
        """)


def index(request):
    template = Template()
    template.field_type_list.append(FieldType('Unit', 'text', 'unit'))
    template.field_type_list.append(FieldType('Value', 'number', 'value', False))
    return render(request, 'core/template_form.html', context={'template': template})
