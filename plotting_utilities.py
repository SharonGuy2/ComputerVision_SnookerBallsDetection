from balls_utilities import mask_balls
import matplotlib.pyplot as plt


def plot_corners_image(
        frame_refference_lines,
        table_corners
):
    plt.imshow(frame_refference_lines)
    plt.title("4 table corners")
    for pt in table_corners:
        plt.plot(pt[0], pt[1], 'ob', markeredgecolor='w', markersize=8)


def plot_masks_for_balls(
        balls_references
):
    plt.figure(figsize=(16, 10))
    plt.subplot(3, 3, 1)
    plt.imshow(balls_references[0])
    plt.title("YELLOW MASK")

    plt.subplot(3, 3, 2)
    plt.imshow(balls_references[1])
    plt.title("BLUE MASK")

    plt.subplot(3, 3, 3)
    plt.imshow(balls_references[2])
    plt.title("GREEN MASK")

    plt.subplot(3, 3, 4)
    plt.imshow(balls_references[3])
    plt.title("PINK MASK")

    plt.subplot(3, 3, 5)
    plt.imshow(balls_references[4])
    plt.title("BROWN MASK")

    plt.subplot(3, 3, 6)
    plt.imshow(balls_references[5])
    plt.title("BLACK MASK")

    plt.subplot(3, 3, 7)
    plt.imshow(balls_references[6])
    plt.title("WHITE MASK")

    plt.show()


def plot_balls_locations(
        frame_refference_rgb,
        balls_references,
        yellow_loc,
        blue_loc,
        green_loc,
        pink_loc,
        brown_loc,
        black_loc,
        white_loc
):
    plt.figure(figsize=(16, 12))
    plt.subplot(3, 3, 1)
    plt.imshow(frame_refference_rgb)
    plt.title("First Frame")

    plt.subplot(3, 3, 2)
    plt.imshow(balls_references[0])
    plt.title("yellow location")
    plt.plot(yellow_loc[0][0][0], yellow_loc[0][0][1], 'or', markeredgecolor='r', markersize=4)

    plt.subplot(3, 3, 3)
    plt.imshow(balls_references[1])
    plt.title("blue location")
    plt.plot(blue_loc[0][0][0], blue_loc[0][0][1], 'or', markeredgecolor='r', markersize=4)

    plt.subplot(3, 3, 4)
    plt.imshow(balls_references[2])
    plt.title("green location")
    plt.plot(green_loc[0][0][0], green_loc[0][0][1], 'or', markeredgecolor='r', markersize=4)

    plt.subplot(3, 3, 5)
    plt.imshow(balls_references[3])
    plt.title("pink location")
    plt.plot(pink_loc[0][0][0], pink_loc[0][0][1], 'or', markeredgecolor='r', markersize=4)

    plt.subplot(3, 3, 6)
    plt.imshow(balls_references[4])
    plt.title("brown location")
    plt.plot(brown_loc[0][0][0], brown_loc[0][0][1], 'or', markeredgecolor='r', markersize=4)

    plt.subplot(3, 3, 7)
    plt.imshow(balls_references[5])
    plt.title("black location")
    plt.plot(black_loc[0][0][0], black_loc[0][0][1], 'or', markeredgecolor='r', markersize=4)

    plt.subplot(3, 3, 8)
    plt.imshow(balls_references[6])
    plt.title("white location")
    plt.plot(white_loc[0][0][0], white_loc[0][0][1], 'or', markeredgecolor='r', markersize=4)

    plt.show()


def plot_frame_with_masks_of_balls(
        yellow_ref,
        blue_ref,
        green_ref,
        pink_ref,
        brown_ref,
        black_ref,
        white_ref
):
    plt.figure(figsize=(20, 12))
    plt.subplot(3, 3, 1)
    plt.imshow(yellow_ref)
    plt.title("yellow ball color mask (first frame)")

    plt.subplot(3, 3, 2)
    plt.imshow(blue_ref)
    plt.title("blue ball color mask (first frame)")

    plt.subplot(3, 3, 3)
    plt.imshow(green_ref)
    plt.title("green ball color mask (first frame)")

    plt.subplot(3, 3, 4)
    plt.imshow(pink_ref)
    plt.title("pink ball color mask (first frame)")

    plt.subplot(3, 3, 5)
    plt.imshow(brown_ref)
    plt.title("brown ball color mask (first frame)")

    plt.subplot(3, 3, 6)
    plt.imshow(black_ref)
    plt.title("black ball color mask (first frame)")

    plt.subplot(3, 3, 7)
    plt.imshow(white_ref)
    plt.title("white ball color mask (first frame)")

    plt.show()
