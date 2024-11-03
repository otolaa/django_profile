from django import template, get_version

register = template.Library()

@register.filter()
def counts(item):
    return len(item)

@register.filter()
def price(num):
    return f"{str(num).replace(',', '.').replace('.00', '')} ₽"

@register.filter()
def hidden_phone(phone, is_user_order = False):
    if is_user_order == False:
        return f"{phone[:2]} (***) *** {phone[-4:]}"
    else:
        return phone

@register.filter()
def hidden_email(email, is_user_order = False):
    if is_user_order == False:
        return f"{email[:3]} *** @ *** {email[-3:]}"
    else:
        return email

@register.filter()
def hidden_text(text, is_user_order = False):
    if is_user_order == False:
        lt_ = round(len(text) / 3)
        return f"*** {text[lt_:lt_ * 2]} ***"
    else:
        return text

@register.filter()
def get_class(request_path):
    """ / == main && /post/ = post & return main_class_page """
    list_style = request_path.split('/')[:2]
    return f"main{'_'.join(list_style)}_page"

@register.filter()
def get_tag(tizer, arg = 'description'):
    for tiz in tizer:
        if tiz.slug == arg:
            return tiz.body
    return False

# {% get_django_version as djv %} <small>django_version: {{ djv }}</small>
@register.simple_tag()
def get_django_version():
    """Вывод версии django"""
    return get_version()