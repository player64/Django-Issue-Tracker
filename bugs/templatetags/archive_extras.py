from django import template

register = template.Library()


@register.filter(name='readable_status')
def readable_status(status):
    defined_status = {
        'todo': 'To do',
        'doing': 'Doing',
        'done': 'Done'
    }

    return defined_status[status] if status in defined_status else ''


@register.filter(name='bootstrap_status')
def bootstrap_status(status):
    statuses = {
        'success': 'success',
        'error': 'danger',
        'warning': 'warning'
    }
    return statuses[status] if status in statuses else ''


@register.filter(name='active_helper')
def active_helper(request_path, expected):
    return request_path.startswith(expected)
