# this will check file extensions 
from os.path import splitext
import PIL.Image
from sys import argv, exit


def main():
    # we should use try becouse user can give less than 2 arguments
    try:
        # we will handele more than 2 arguments in the function
        is_valid_input(argv[1], argv[2])
    except IndexError:
        exit("Too few command-line arguments")

    # maybe specified file is non existing, we should use try
    try:
        # with this trick i can open 2 files at once
        with (PIL.Image.open(argv[1]) as before, PIL.Image.open("shirt.png") as shirt):

            # this will give be a tuple(width, height)
            size = shirt.size
            # this will resize users image and make it the same size as shirt
            # firts argument is image to resize
            # second one is new size for image
            smaller_before = PIL.ImageOps.fit(before, size)

            # past shirt to the smaller_before image
            # wherein the first shirt represents the image to overlay
            # the second shirt represents a “mask” indicating which pixels in photo to update.
            # optional arguments are default value
            smaller_before.paste(shirt, shirt)
            # save image with name in parenrhesis
            smaller_before.save(argv[2])

    except FileNotFoundError:
        exit("File does not exist")


def is_valid_input(input, output):
    if len(argv) > 3:
        exit("Too many command-line arguments")

    elif not splitext(input)[1] in [".jpg", ".jpeg", ".png"]:
        exit("File formats should be .jpg .jpeg or .png")

    elif not splitext(output)[1] in [".jpg", ".jpeg", ".png"]:
        exit("File formats should be .jpg .jpeg or .png")

    elif splitext(input)[1] != splitext(output)[1]:
        exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
