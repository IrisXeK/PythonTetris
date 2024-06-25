class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)

    @classmethod
    def get_cell_colors(cls):  # 用装饰符直接操控类而不是类的实例,cls指类本身 类比与self self是实例级的,cls是类级的操作
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.cyan, cls.blue]
