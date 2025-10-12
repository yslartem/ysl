import os
from moviepy.editor import *

# Пути к папкам
folder_images = 'images'  # папка с изображениями
folder_audio = 'audio'    # папка с аудиофайлами
folder_output = 'output_videos'  # папка для сохранения видео

if not os.path.exists(folder_output):
    os.makedirs(folder_output)

width, height = 1920, 1080

def create_video(image_path, audio_path, output_path):
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration

    img_clip = ImageClip(image_path).set_duration(duration)
    img_clip = img_clip.resize(height=height * 0.8)  # масштабируем картинку по высоте
    background = ColorClip(size=(width, height), color=(0, 0, 0), duration=duration)

    img_clip = img_clip.set_position('center')
    video_clip = CompositeVideoClip([background, img_clip])
    video_clip = video_clip.set_audio(audio_clip)

    video_clip.write_videofile(output_path, fps=24)

audio_files = [f for f in os.listdir(folder_audio) if f.lower().endswith(('.mp3', '.wav', '.aac', '.m4a', '.ogg'))]
image_files = [f for f in os.listdir(folder_images) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not image_files:
    print('Нет изображений для создания видео.')
else:
    image_path = os.path.join(folder_images, image_files[0])
    for audio_file in audio_files:
        audio_path = os.path.join(folder_audio, audio_file)
        output_file = os.path.splitext(audio_file)[0] + '.mp4'
        output_path = os.path.join(folder_output, output_file)
        create_video(image_path, audio_path, output_path)
