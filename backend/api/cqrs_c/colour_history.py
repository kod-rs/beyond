from backend.api.model.colourHistory import ColourHistory


def update_or_create_colour_history(colour_hex):
    ch, _ = ColourHistory.objects.update_or_create(
        colour=colour_hex,
        defaults={"colour": colour_hex}
    )
    ch.save()
    return ch
