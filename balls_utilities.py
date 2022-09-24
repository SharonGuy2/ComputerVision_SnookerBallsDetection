import numpy as np
from colors_ranges import *
import cv2


def mask_by_color_range(
        img,
        color_range,
        sat_range=[50, 255],
        v_range=[50, 255],
        table_mask=None
):
    lower = np.array([color_range[0], sat_range[0], v_range[0]])
    upper = np.array([color_range[1], sat_range[1], v_range[1]])
    img_mask = cv2.inRange(img, lower, upper)
    img_mask = np.maximum(img_mask, table_mask)
    return img_mask


def mask_black_ball(img, table_mask):
    lower = np.array([0, 200, 0])
    upper = np.array([180, 255, 120])
    img_mask = cv2.inRange(img, lower, upper)
    img_mask = np.maximum(img_mask, table_mask)
    return img_mask


def mask_white_ball(img, table_mask):
    lower = np.array([0, 0, 230])
    upper = np.array([60, 200, 255])
    img_mask = cv2.inRange(img, lower, upper)
    img_mask = np.maximum(img_mask, table_mask)
    return img_mask


def create_balls_masks(
        table_mask,
        frame_refference_hsv
):
    yellow = mask_by_color_range(
        frame_refference_hsv,
        YELLOW_H_RANGE,
        table_mask=table_mask)

    blue = mask_by_color_range(
        frame_refference_hsv,
        BLUE_H_RANGE,
        table_mask=table_mask
    )

    green = mask_by_color_range(
        frame_refference_hsv,
        GREEN_H_RANGE,
        table_mask=table_mask
    )

    pink = mask_by_color_range(
        frame_refference_hsv,
        PINK_H_RANGE,
        PINK_SAT_RANGE,
        PINK_V_RANGE,
        table_mask=table_mask
    )

    brown = mask_by_color_range(
        frame_refference_hsv,
        BROWN_H_RANGE,
        BROWN_SAT_RANGE,
        BROWN_V_RANGE,
        table_mask=table_mask
    )

    black = mask_black_ball(
        frame_refference_hsv,
        table_mask=table_mask
    )

    white = mask_white_ball(
        frame_refference_hsv,
        table_mask=table_mask
    )

    return yellow, blue, green, pink, brown, black, white


def mask_balls(img_mask, frame_refference):
    img_mask_3ch = np.zeros_like(frame_refference)
    img_mask_3ch[:, :, 0] = img_mask
    img_mask_3ch[:, :, 1] = img_mask
    img_mask_3ch[:, :, 2] = img_mask
    img = np.minimum(img_mask_3ch, frame_refference)
    return img


def get_masks_for_balls(
        frame_refference_rgb,
        balls_references
):
    yellow_ref = mask_balls(balls_references[0], frame_refference_rgb)
    blue_ref = mask_balls(balls_references[1], frame_refference_rgb)
    green_ref = mask_balls(balls_references[2], frame_refference_rgb)
    pink_ref = mask_balls(balls_references[3], frame_refference_rgb)
    brown_ref = mask_balls(balls_references[4], frame_refference_rgb)
    black_ref = mask_balls(balls_references[5], frame_refference_rgb)
    white_ref = mask_balls(balls_references[6], frame_refference_rgb)

    return yellow_ref, blue_ref, green_ref, pink_ref, brown_ref, black_ref, white_ref


def _pt_in_list(pt0, pt_list):
    for pt in pt_list:
        if (pt[0] - 5 < pt0[0] < pt[0] + 5) and (pt[1] - 5 < pt0[1] < pt[1] + 5):
            return True
    return False


def find_ball(
        mask,
        ball_list,
        table_corners
):
    # Opening - morphology
    kernel = np.ones((3, 3), np.uint8)
    mask_erosion = cv2.erode(mask, kernel)
    mask_dilation = cv2.dilate(mask_erosion, kernel)

    # Find balls using Hough circles
    balls_circles = cv2.HoughCircles(mask_dilation, method=cv2.HOUGH_GRADIENT,
                                     dp=1, minDist=20, param1=160, param2=8, minRadius=3, maxRadius=9)

    # In case we found no balls - return False
    if balls_circles is None:
        print(f'no balls : {balls_circles}')
        return False

    balls_circles = balls_circles.astype(np.int)

    for (x, y, rad) in balls_circles[0]:
        # Make sure circle is not outside table area
        if (np.min(table_corners[:, :, 0]) < x < np.max(table_corners[:, :, 0])) and (
                np.min(table_corners[:, :, 1]) < y < np.max(table_corners[:, :, 1])):
            # Make sure circle coordinates doesn't already exists in ball_list
            if not (_pt_in_list((x, y), ball_list)):
                ball_loc = ((x, y))
                ball_list.append((x, y))
                break

    ball_loc = np.int32(ball_loc).reshape(-1, 1, 2)
    ball_loc = ball_loc.astype(np.float32)

    return ball_loc


def get_balls_locations(
        balls_references,
        table_corners
):
    balls_list = []
    yellow_loc = find_ball(
        balls_references[0], balls_list, table_corners=table_corners)
    blue_loc = find_ball(
        balls_references[1], balls_list, table_corners=table_corners)
    green_loc = find_ball(
        balls_references[2], balls_list, table_corners=table_corners)
    pink_loc = find_ball(
        balls_references[3], balls_list, table_corners=table_corners)
    brown_loc = find_ball(
        balls_references[4], balls_list, table_corners=table_corners)
    black_loc = find_ball(
        balls_references[5], balls_list, table_corners=table_corners)
    white_loc = find_ball(
        balls_references[6], balls_list, table_corners=table_corners)

    black_ball_reff = black_loc

    return (yellow_loc, blue_loc, green_loc, pink_loc, brown_loc, black_loc, white_loc), black_ball_reff, balls_list


def build_list_of_mask_location_tuples(
        balls_references,
        balls_locations
):
    """
    Returns:
        List[Tuple(reference,location)]
    """
    yellow = (balls_references[0], balls_locations[0])
    blue = (balls_references[1], balls_locations[1])
    green = (balls_references[2], balls_locations[2])
    pink = (balls_references[3], balls_locations[3])
    brown = (balls_references[4], balls_locations[4])
    black = (balls_references[5], balls_locations[5])
    white = (balls_references[6], balls_locations[6])

    return [yellow, blue, green, pink, brown, black, white]


def mask_white_ball_for_tracking(
        img,
        table_mask
):
    lower = np.array([0, 55, 245])
    upper = np.array([180, 255, 255])
    img_mask = cv2.inRange(img, lower, upper)
    img_mask = np.maximum(img_mask, table_mask)
    return img_mask


def paint_ball_on_view(top_view, ball_color, coordinates):
    for idx, ball in enumerate(coordinates):
        cv2.circle(top_view, (ball[0][0], ball[0][1]), 6, ball_color, -1)
        cv2.circle(top_view, (ball[0][0], ball[0][1]), 7, (0, 0, 0), 1)
    return top_view
