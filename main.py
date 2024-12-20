import cv2
import datetime


def read_annotations(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


first_annotations = read_annotations('data/1.txt')
second_annotations = read_annotations('data/2.txt')
third_annotations = read_annotations('data/3.txt')
fourth_annotations = read_annotations('data/4.txt')

first_video = cv2.VideoCapture("data/1.avi")
second_video = cv2.VideoCapture("data/2.avi")
third_video = cv2.VideoCapture("data/3.avi")
fourth_video = cv2.VideoCapture("data/4.avi")

frame_index1 = 0
frame_index2 = 0
frame_index3 = 0
frame_index4 = 0

fps = 5
delay = int(1000 / fps)

# Хранение предыдущих кадров
prev_frame1 = None
prev_frame2 = None
prev_frame3 = None
prev_frame4 = None

while True:
    ret1, frame1 = first_video.read()
    ret2, frame2 = second_video.read()
    ret3, frame3 = third_video.read()
    ret4, frame4 = fourth_video.read()

    # Изменение размера кадров для удобства отображения
    if ret1:
        frame1 = cv2.resize(frame1, (640, 480))
        if frame_index1 < len(first_annotations):
            annotation_float = float(first_annotations[frame_index1])
            annotation_date = datetime.datetime.fromtimestamp(annotation_float / 1000)
            complete_date = str(annotation_date.strftime('%H:%M:%S.%f'))
            cv2.putText(frame1, complete_date, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        prev_frame1 = frame1  # Сохраняем текущий кадр как предыдущий
    else:
        frame1 = prev_frame1  # Используем предыдущий кадр, если текущий не доступен

    if ret2:
        frame2 = cv2.resize(frame2, (640, 480))
        if frame_index2 < len(second_annotations):
            annotation_float = float(second_annotations[frame_index2])
            annotation_date = datetime.datetime.fromtimestamp(annotation_float / 1000)
            complete_date = str(annotation_date.strftime('%H:%M:%S.%f'))
            cv2.putText(frame1, complete_date, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        prev_frame2 = frame2
    else:
        frame2 = prev_frame2

    if ret3:
        frame3 = cv2.resize(frame3, (640, 480))
        if frame_index3 < len(third_annotations):
            annotation_float = float(third_annotations[frame_index3])
            annotation_date = datetime.datetime.fromtimestamp(annotation_float / 1000)
            complete_date = str(annotation_date.strftime('%H:%M:%S.%f'))
            cv2.putText(frame1, complete_date, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        prev_frame3 = frame3
    else:
        frame3 = prev_frame3

    if ret4:
        frame4 = cv2.resize(frame4, (640, 480))
        if frame_index4 < len(fourth_annotations):
            annotation_float = float(fourth_annotations[frame_index4])
            annotation_date = datetime.datetime.fromtimestamp(annotation_float / 1000)
            complete_date = str(annotation_date.strftime('%H:%M:%S.%f'))
            cv2.putText(frame1, complete_date, (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        prev_frame4 = frame4
    else:
        frame4 = prev_frame4

    # Объединение кадров в одно изображение
    top_row = cv2.hconcat([frame1, frame2])
    bottom_row = cv2.hconcat([frame3, frame4])
    combined_frame = cv2.vconcat([top_row, bottom_row])

    # Отображение объединенного кадра
    cv2.imshow('Synchronized Video Playback', combined_frame)

    # Увеличиваем счетчики кадров, если текущие кадры доступны
    if ret1 and frame_index1 < len(first_annotations):
        frame_index1 += 1
    if ret2 and frame_index2 < len(second_annotations):
        frame_index2 += 1
    if ret3 and frame_index3 < len(third_annotations):
        frame_index3 += 1
    if ret4 and frame_index4 < len(fourth_annotations):
        frame_index4 += 1

    # Выход при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
first_video.release()
second_video.release()
third_video.release()
fourth_video.release()
cv2.destroyAllWindows()
