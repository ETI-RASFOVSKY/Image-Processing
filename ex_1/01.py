import sys
from PIL import Image


def show_channel_gray(channel, name):
    print(f"Showing {name} channel (grayscale)...")
    try:
        channel.show(title=f"{name} (grayscale)")
    except TypeError:
        channel.show()


def show_channel_color(channel, name):
    print(f"Showing {name} channel (colorized)...")
    zero = Image.new('L', channel.size, 0)
    if name == 'R':
        color_img = Image.merge('RGB', (channel, zero, zero))
    elif name == 'G':
        color_img = Image.merge('RGB', (zero, channel, zero))
    elif name == 'B':
        color_img = Image.merge('RGB', (zero, zero, channel))
    else:
        color_img = channel
    try:
        color_img.show(title=f"{name} (color)")
    except TypeError:
        color_img.show()


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} image-filename")
        exit(-1)

    file_name = sys.argv[1]
    try:
        img = Image.open(file_name)
    except Exception as e:
        print(f"Error opening '{file_name}': {e}")
        exit(-1)

    print(f"Loaded '{file_name}', mode={img.mode}, size={img.size}")

    orig_mode = img.mode

    if orig_mode == 'L':
        print("Image is grayscale (single channel). Showing image.")
        try:
            img.show(title="Grayscale")
        except TypeError:
            img.show()
        return

    if orig_mode not in ('RGB', 'RGBA'):
        img = img.convert('RGB')
        orig_mode = 'RGB'

    channels = img.split()

    if orig_mode == 'RGBA':
        names = ('R', 'G', 'B', 'A')
    else:
        names = ('R', 'G', 'B')

    for ch, name in zip(channels, names):
        show_channel_gray(ch, name)
        if name in ('R', 'G', 'B'):
            show_channel_color(ch, name)


if __name__ == '__main__':
    main()