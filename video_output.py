from tkinter import Label
from moviepy import VideoFileClip
from PIL import Image, ImageTk


class VideoPlayer:
    """
    Класс видеоплеера для проигрывания результрующего видео,
    где 4 рассинхонизированных видео синхронизированы"""
    def __init__(self, master, video_path, fps=5):
        self.master = master
        self.master.title("Video Player")
        self.fps = fps

        # Загрузка видео
        self.clip = VideoFileClip(video_path)
        self.frame_count = int(self.clip.fps * self.clip.duration)

        # Создание метки для отображения видео
        self.label = Label(master)
        self.label.pack()

        self.current_frame = 0
        self.update_frame()

    def change_speed(self, speed):
        """Метод для смены скорости"""
        self.fps = speed

    def update_frame(self):
        """Метод смены фрейма"""
        if self.current_frame < self.frame_count:
            # Получение текущего кадра
            frame = self.clip.get_frame(self.current_frame / self.clip.fps)
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(frame)

            # Обновление метки с новым кадром
            self.label.config(image=frame)
            self.label.image = frame

            # Переход к следующему кадру
            self.current_frame += 1
            self.master.after(int(1000 / self.fps), self.update_frame)
