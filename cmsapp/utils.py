def is_admin_or_compuser(user):
    return user.is_superuser or user.groups.filter(name='compuser').exists()
