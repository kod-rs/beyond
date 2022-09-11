"""

i, _ = Portfolio.objects.update_or_create(
    username=username, name=current_name,
    defaults={"name": new_name, "colour": colour}
)
i.save()

"""
