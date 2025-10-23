import tkinter as tk
import math

start_length = 100
length_ratio = 0.7
angle = 30
min_length = 5


def draw_branch(canvas, x, y, length, angle_deg, depth):
    """Рекурсивная функция для рисования ветки"""
    if length < min_length:
        return

    # Вычисляем конечные координаты
    angle_rad = math.radians(angle_deg)
    end_x = x + length * math.cos(angle_rad)
    end_y = y + length * math.sin(angle_rad)

    # Цвет в зависимости от глубины
    colors = ['#8B4513', '#A0522D', '#CD853F', '#D2691E', '#F4A460',
              '#DEB887', '#D2B48C', '#BC8F8F', '#F5DEB3', '#FFE4C4']
    color = colors[min(depth, len(colors) - 1)]

    # Рисуем ветку
    canvas.create_line(x, y, end_x, end_y, width=max(1, length / 20), fill=color)

    # Новая длина
    new_length = length * length_ratio

    # Рекурсивно рисуем левую и правую ветки
    draw_branch(canvas, end_x, end_y, new_length, angle_deg - angle, depth + 1)
    draw_branch(canvas, end_x, end_y, new_length, angle_deg + angle, depth + 1)


def draw_tree():
    """Очищает холст и рисует дерево"""
    canvas.delete("all")
    start_x = 400
    start_y = 500
    draw_branch(canvas, start_x, start_y, start_length, -90, 0)


def update_angle(value):
    """Обновляет угол и перерисовывает дерево"""
    global angle
    angle = int(value)
    angle_label.config(text=f"Угол: {angle}°")
    draw_tree()


# Создаем главное окно
root = tk.Tk()
root.title("Фрактальное дерево")
root.geometry("800x700")

# Создаем холст
canvas = tk.Canvas(root, width=800, height=600, bg='white')
canvas.pack()

# Надпись с текущим углом
angle_label = tk.Label(root, text=f"Угол: {angle}°")
angle_label.pack()

# Слайдер для изменения угла
angle_scale = tk.Scale(root, from_=10, to=60, orient=tk.HORIZONTAL, command=update_angle)
angle_scale.pack(fill=tk.X, padx=20)

redraw_button = tk.Button(root, text="Перерисовать", command=draw_tree)
redraw_button.pack()

draw_tree()

root.mainloop()
