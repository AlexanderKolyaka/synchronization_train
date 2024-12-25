import video_processing
import tkinter as tk
import cv2
from video_output import VideoPlayer

# Задаем параметры видео
WIDTH, HEIGHT = 640, 480  # Размеры видео
FPS = 5  # Частота кадров
OUTPUT_FILE = 'data/out.avi'  # Имя выходного файла
FOURCC = cv2.VideoWriter_fourcc(*'XVID')  # Кодек для AVI
out = cv2.VideoWriter(OUTPUT_FILE, FOURCC, FPS, (WIDTH * 2, HEIGHT * 2))


def create_buttons():
    """Метод создания кнопок"""
    btn_normal = tk.Button(
                    root, text="Нормальная скорость",
                    command=lambda: player.change_speed(5))
    btn_normal.pack(side="left", padx=5, pady=5)

    btn_half = tk.Button(
                root, text="Половинная скорость",
                command=lambda: player.change_speed(100))
    btn_half.pack(side="left", padx=5, pady=5)

    btn_double = tk.Button(
                    root, text="Двойная скорость",
                    command=lambda: player.change_speed(1000))
    btn_double.pack(side="left", padx=5, pady=5)


if __name__ == '__main__':
    video_processing.release_video(out)
    root = tk.Tk()
    create_buttons()
    video_path = OUTPUT_FILE  # Замените на путь к вашему видео
    player = VideoPlayer(root, video_path)
    root.mainloop()
