from . import register

@register.filter
def index(indexable, i):
    return indexable[i-1]