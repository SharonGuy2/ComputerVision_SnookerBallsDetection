import numpy as np
import cv2


def create_2d_top_view(frame_refference_rgb):
    h = frame_refference_rgb.shape[0]
    w = int(h / 2)
    top_view = np.zeros((h, w, 3), np.uint8)
    top_view[:, :] = (0, 153, 76)  # Fill table with green color
    cv2.line(top_view, (0, h - 1), (w - 1, h - 1), (0, 0, 255), 5)
    cv2.line(top_view, (0, h - 1), (0, 0), (0, 0, 255), 5)
    cv2.line(top_view, (w - 1, 0), (0, 0), (0, 0, 255), 5)
    cv2.line(top_view, (w - 1, 0), (w - 1, h - 1), (0, 0, 255), 5)
    return top_view


def draw_table_borders(
        canvas,
        pt_list
):
    pt1, pt2, pt3, pt4 = pt_list[0][0], pt_list[1][0], pt_list[2][0], pt_list[3][0]
    cv2.line(canvas, (int(pt1[0]), int(pt1[1])),
             (int(pt3[0]), int(pt3[1])), (0, 0, 255), 3)
    cv2.line(canvas, (int(pt2[0]), int(pt2[1])),
             (int(pt3[0]), int(pt3[1])), (0, 0, 255), 3)
    cv2.line(canvas, (int(pt2[0]), int(pt2[1])),
             (int(pt4[0]), int(pt4[1])), (0, 0, 255), 3)
    cv2.line(canvas, (int(pt4[0]), int(pt4[1])),
             (int(pt1[0]), int(pt1[1])), (0, 0, 255), 3)
    return canvas


def line_intersection(
        line1, line2
):
    def _detect(a, b):
        return a[0] * b[1] - a[1] * b[0]

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    div = _detect(xdiff, ydiff)

    d = (_detect(*line1), _detect(*line2))
    x = _detect(d, xdiff) / div
    y = _detect(d, ydiff) / div
    return ((x), (y))
