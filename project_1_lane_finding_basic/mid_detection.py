from Line import Line
import numpy as np

def get_mid_line(left_lane: Line, right_lane:Line):
    left_coords = left_lane.get_coords()
    right_coords = right_lane.get_coords()
    mid_x1 = (right_coords[0]-left_coords[0])/2
    mid_x2 = (right_coords[2]-left_coords[2])/2
    mid_y1 = right_coords[1]
    mid_y2 = right_coords[3]

    mid_lane = Line(mid_x1, mid_y1, mid_x2, mid_y2)
    return mid_lane
