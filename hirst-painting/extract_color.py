import colorgram


def extract_colors(image_path, numer_of_color):
    """

    :param image_path: the path of the image you want to extract color from it
    :param numer_of_color: the number of the color you want to extract
    :return: a list of color rgb  values
    """
    rgb_color = []
    colors = colorgram.extract(image_path, numer_of_color)

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_color.append((r, g, b))
    return rgb_color
