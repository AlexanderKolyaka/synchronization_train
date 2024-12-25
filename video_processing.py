import cv2
import datetime

READ_FPS = 5


# Открытие видео
first_video = cv2.VideoCapture("data/1.avi")
second_video = cv2.VideoCapture("data/2.avi")
third_video = cv2.VideoCapture("data/3.avi")
fourth_video = cv2.VideoCapture("data/4.avi")


def read_annotations(filename):
    """Чтение аннотаций из файла."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def show_result(annotation, index_annotation):
    """Форматирование временной метки для отображения."""
    annotation_float = float(annotation[index_annotation])
    annotation_date = datetime.datetime.fromtimestamp(annotation_float)
    complete_date = str(annotation_date.strftime('%H:%M:%S:%f'))
    return complete_date


# Чтение аннотаций
first_annotations = read_annotations('data/1.txt')
second_annotations = read_annotations('data/2.txt')
third_annotations = read_annotations('data/3.txt')
fourth_annotations = read_annotations('data/4.txt')
prev_frame1 = prev_frame2 = prev_frame3 = prev_frame4 = None


def release_video(out):
    ret1, frame1 = first_video.read()
    ret2, frame2 = second_video.read()
    ret3, frame3 = third_video.read()
    ret4, frame4 = fourth_video.read()
    frame_index1 = frame_index2 = frame_index3 = frame_index4 = 0

    while (frame_index1 <= len(first_annotations) - 1 and
            frame_index2 <= len(second_annotations) - 1 and
            frame_index3 <= len(third_annotations) - 1 and
            frame_index4 <= len(fourth_annotations) - 1):
        # Получаем временные метки
        timestamp_sec1 = float(first_annotations[frame_index1])
        timestamp_sec2 = float(second_annotations[frame_index2])
        timestamp_sec3 = float(third_annotations[frame_index3])
        timestamp_sec4 = float(fourth_annotations[frame_index4])

        # Если все видео закончились, выходим из цикла
        if not (ret1 or ret2 or ret3 or ret4):
            break

        # Обработка кадров
        if ret1:
            frame1 = cv2.resize(frame1, (640, 480))
            if frame_index1 < len(first_annotations):
                cv2.putText(frame1, f'1: {show_result(first_annotations, frame_index1)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            prev_frame1 = frame1
        else:
            frame1 = prev_frame1

        if ret2:
            frame2 = cv2.resize(frame2, (640, 480))
            if frame_index2 < len(second_annotations):
                cv2.putText(frame1, f'2: {show_result(second_annotations, frame_index2)}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            prev_frame2 = frame2
        else:
            frame2 = prev_frame2

        if ret3:
            frame3 = cv2.resize(frame3, (640, 480))
            if frame_index3 < len(third_annotations):
                cv2.putText(frame1, f'3: {show_result(third_annotations, frame_index3)}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            prev_frame3 = frame3
        else:
            frame3 = prev_frame3

        if ret4:
            frame4 = cv2.resize(frame4, (640, 480))
            if frame_index4 < len(fourth_annotations):
                cv2.putText(frame1, f'4: {show_result(fourth_annotations, frame_index4)}', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            prev_frame4 = frame4
        else:
            frame4 = prev_frame4

        # Проверка на синхронизацию с небольшим отклонением
        timestamps = [
            timestamp_sec1, timestamp_sec2, timestamp_sec3, timestamp_sec4
            ]
        min_timestamp = min(timestamps)
        max_timestamp = max(timestamps)
        max_index = timestamps.index(max_timestamp)

        if max_timestamp - min_timestamp >= 0.3:
            # Объединение кадров в одно изображение
            if max_index == 0:
                frame1 = prev_frame1
                frame_index2 += 1
                frame_index3 += 1
                frame_index4 += 1
            elif max_index == 1:
                frame2 = prev_frame2
                frame_index1 += 1
                frame_index3 += 1
                frame_index4 += 1
            elif max_index == 2:
                frame3 = prev_frame3
                frame_index2 += 1
                frame_index1 += 1
                frame_index4 += 1
            else:
                frame4 = prev_frame4
                frame_index2 += 1
                frame_index3 += 1
                frame_index1 += 1
            top_row = cv2.hconcat([frame1, frame2])
            bottom_row = cv2.hconcat([frame3, frame4])
            combined_frame = cv2.vconcat([top_row, bottom_row])
            # Записываем кадр в видео
            out.write(combined_frame)
            # Объединение кадров в одно изображение
            if max_index == 0:
                ret2, frame2 = second_video.read()
                ret3, frame3 = third_video.read()
                ret4, frame4 = fourth_video.read()
            elif max_index == 1:
                ret1, frame1 = first_video.read()
                ret3, frame3 = third_video.read()
                ret4, frame4 = fourth_video.read()
            elif max_index == 2:
                ret1, frame1 = first_video.read()
                ret2, frame2 = second_video.read()
                ret4, frame4 = fourth_video.read()
            else:
                ret1, frame1 = first_video.read()
                ret2, frame2 = second_video.read()
                ret3, frame3 = third_video.read()
        else:
            frame_index1 += 1
            frame_index2 += 1
            frame_index3 += 1
            frame_index4 += 1
            # Если видео не синхронизированы, показываем текущие кадры
            current_frame = cv2.hconcat([frame1, frame2])
            current_frame = cv2.vconcat(
                [current_frame, cv2.hconcat([frame3, frame4])]
                )
            ret1, frame1 = first_video.read()
            ret2, frame2 = second_video.read()
            ret3, frame3 = third_video.read()
            ret4, frame4 = fourth_video.read()

    # Освобождение ресурсов
    first_video.release()
    second_video.release()
    third_video.release()
    fourth_video.release()
    out.release()
    cv2.destroyAllWindows()
