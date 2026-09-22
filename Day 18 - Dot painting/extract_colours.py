import colorgram

colours = colorgram.extract('hirst_painting.jpg', 30)
colour_list = []
for c in colours:
    colour = c.rgb
    colour_list.append((colour.r, colour.g, colour.b))

print(colour_list)