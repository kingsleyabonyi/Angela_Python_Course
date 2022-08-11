
# 


# collect_height = int(input("Height of the wall"))
# collect_weight = int(input("width of wall"))
# coverage = 5

def paint_cal(height, width, cover):
    area = height * width
    num_0f_can = round(area / cover)
    print(f"YOu will need {num_0f_can} can for the painting")

paint_cal(3, 7, 5)
