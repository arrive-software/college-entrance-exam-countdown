import turtle
import time

# ================== 配置目标时间 ==================
# 格式："年-月-日 时:分:秒" (24小时制)
TARGET_STR = "2027-01-01 00:00:00"
# =================================================

def countdown_to_datetime():
    target_timestamp = 1812330000

    # 2. 初始化 Turtle 窗口
    screen = turtle.Screen()
    screen.title("高考倒计时")
    screen.bgcolor("black")
    screen.setup(width=600, height=400)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color("#FFFFFF")
    pen.goto(0, -60)

    def update():
        # 3. 用 time.time() 获取当前时间戳（精确到秒的小数，我们取整秒忽略毫秒）
        now_timestamp = time.time()
        remaining_seconds = target_timestamp - now_timestamp

        if remaining_seconds <= 0:
            pen.clear()
            pen.write("时间到！", align="center",
                      font=("Arial", 50, "bold"))
            return

        # 4. 转换为 天、时、分、秒
        total_seconds = int(remaining_seconds)  # 向下取整，显示整数秒
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        secs = total_seconds % 60

        # 5. 显示格式：X天 HH:MM:SS
        display_text = f"距离高考还有：\n{days}天 \n{hours:02d}时{minutes:02d}分{secs:02d}秒"
        pen.clear()
        pen.write(display_text, align="center",
                  font=("Microsoft YaHe", 48, "bold"))

        # 6. 大约 1 秒后再次调用（用 ontimer 让界面不卡顿）
        screen.ontimer(update, 100)

    update()
    screen.mainloop()

# 运行倒计时
countdown_to_datetime()
