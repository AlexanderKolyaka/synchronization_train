import cv2

# Загрузка видео
cap1 = cv2.VideoCapture("data/1.avi")
cap2 = cv2.VideoCapture("data/2.avi")
cap3 = cv2.VideoCapture("data/3.avi")
cap4 = cv2.VideoCapture("data/4.avi")

while True:
    # Чтение кадров из каждого видео
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    ret4, frame4 = cap4.read()

    # Проверка, были ли успешно считаны кадры
    if not ret1 or not ret2 or not ret3 or not ret4:
        break

    # Изменение размера кадров для удобства отображения (по желанию)
    frame1 = cv2.resize(frame1, (320, 240))
    frame2 = cv2.resize(frame2, (320, 240))
    frame3 = cv2.resize(frame3, (320, 240))
    frame4 = cv2.resize(frame4, (320, 240))

    # Объединение кадров в одно изображение
    top_row = cv2.hconcat([frame1, frame2])  # Объединяем первые два видео
    bottom_row = cv2.hconcat([frame3, frame4])  # Объединяем вторые два видео
    combined_frame = cv2.vconcat([top_row, bottom_row])  # Объединяем две строки

    # Отображение объединенного кадра
    cv2.imshow('Synchronized Video Playback', top_row)

    # Выход при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap1.release()
cap2.release()
cap3.release()
cap4.release()
cv2.destroyAllWindows()