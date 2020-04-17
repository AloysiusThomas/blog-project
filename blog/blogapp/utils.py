def article_image_location(instance, filename):
    try:
        extension = filename.split(".")[1].lower()
        extension = "." + extension
    except Exception as e:
        print(e, "Handled")
        extension = ""
    filename = str(instance.title)
    filename = filename.replace(" ", "-")
    filename = filename + extension
    location = "article/images/"
    return '%s/%s' % (location, filename)


def article_extra_image_location(instance, filename):
    try:
        extension = filename.split(".")[1].lower()
        extension = "." + extension
    except Exception as e:
        print(e, "Handled")
        extension = ""
    filename = str(instance.article.title)
    filename = filename.replace(" ", "-")
    filename = filename + extension
    location = "article/images/extra/"
    return '%s/%s' % (location, filename)
