from PIL import Image


current_value = int(input("Current value: "))
max_value = int(input("Max value: "))
colour = tuple(map(int, input("Colour: ").split()))
icon_filename = input("Icon filename: ")
output_filename = input("Output filename: ")

icon_size = 64
bar_height = 64
unit_width = 30
border_width = 3

bar_fill_width = max_value * unit_width
bar_total_width = bar_fill_width + 2 * border_width

img_width = icon_size + bar_total_width + 2 * border_width
img_height = 64 + 2 * border_width
img = Image.new("RGBA", (img_width, img_height), (0, 0, 0, 0))

icon = Image.open(icon_filename)
icon = icon.resize((icon_size, icon_size))

for x in range(icon_size):
    for y in range(icon_size):
        pixel = icon.getpixel((x, y))
        img.putpixel((x + border_width, y + border_width), pixel)

filled_width = current_value * unit_width

bar_left = icon_size + 2 * border_width
bar_top = border_width
bar_bottom = img_height - border_width

for x in range(bar_left, bar_left + bar_fill_width + 2 * border_width):
    for y in range(bar_top):
        img.putpixel((x, y), (0, 0, 0, 255))
    for y in range(bar_bottom, img_height):
        img.putpixel((x, y), (0, 0, 0, 255))

for y in range(bar_top, bar_bottom):
    for x in range(bar_left, bar_left + border_width):
        img.putpixel((x, y), (0, 0, 0, 255))
    for x in range(bar_left + bar_fill_width + border_width, bar_left + bar_fill_width + 2 * border_width):
        img.putpixel((x, y), (0, 0, 0, 255))

for x in range(bar_left + border_width, bar_left + border_width + filled_width):
    for y in range(border_width, bar_bottom):
        img.putpixel((x, y), colour)

img.save(output_filename)

