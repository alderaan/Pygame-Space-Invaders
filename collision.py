def get_bounding_rect(obj):
    if obj.shape == "rect":
        return {"x": obj.x, "y": obj.y, "width": obj.width, "height": obj.height}
    elif obj.shape == "circle":
        return {
            "x": obj.x - obj.radius,
            "y": obj.y - obj.radius,
            "width": 2 * obj.radius,
            "height": 2 * obj.radius,
        }
    elif obj.shape == "polygon":
        min_x = min(point[0] for point in obj.points)
        max_x = max(point[0] for point in obj.points)
        min_y = min(point[1] for point in obj.points)
        max_y = max(point[1] for point in obj.points)
        return {"x": min_x, "y": min_y, "width": max_x - min_x, "height": max_y - min_y}


def check_collision(obj1, obj2):
    rect1 = get_bounding_rect(obj1)
    rect2 = get_bounding_rect(obj2)
    # print(rect1, obj1.y, obj1.shape)
    # print(rect2, obj2.y, obj2.shape)
    return (
        rect1["x"] < rect2["x"] + rect2["width"]
        and rect1["x"] + rect1["width"] > rect2["x"]
        and rect1["y"] < rect2["y"] + rect2["height"]
        and rect1["height"] + rect1["y"] > rect2["y"]
    )
