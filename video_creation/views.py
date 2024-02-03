import shutil
from django.http import HttpResponse
from django.shortcuts import redirect, render
from PIL import Image
import os
import imageio
from moviepy import editor
# from django.core.servers.basehttp import 
from wsgiref.util import FileWrapper
# from django.core.wsgi import FileWrapper


# def home_page(request):
#     if request.method == 'POST':
#         audio_path = 'media/uploaded_audios/'
#         images_path = 'media/uploaded_images/'
#         os.makedirs(audio_path, exist_ok=True)
#         os.makedirs(images_path, exist_ok=True)

#         # Getting Input Audio File
#         audio_file = request.FILES.get('audio')
        
#         # Getting Input Images
#         image_files = request.FILES.getlist('images')

#         if audio_file:
#             saved_audio_path = os.path.join(audio_path, audio_file.name)

#             with open(saved_audio_path, 'wb') as destination:
#                 for chunk in audio_file.chunks():
#                     destination.write(chunk)
                    
#         for image_file in image_files:
#             with open(os.path.join(images_path, image_file.name), 'wb') as destination:
#                 for chunk in image_file.chunks():
#                     destination.write(chunk)

#         # Use moviepy.AudioFileClip directly for Opus support
#         saved_audio_file = os.path.join(audio_path, audio_file.name)
#         audio = editor.AudioFileClip(saved_audio_file)
#         audio_length = audio.duration

#         list_of_images = []
#         for image_file in os.listdir(images_path):
#             if image_file.endswith('.png') or image_file.endswith('.jpg'):
#                 image_path = os.path.join(images_path, image_file)
#                 image = Image.open(image_path).resize((1280, 720), Image.Resampling.LANCZOS)
#                 list_of_images.append(image)

#         duration = audio_length / len(list_of_images)
#         imageio.mimsave('images.gif', list_of_images, fps=1/duration)

#         # Create video from GIF and set the audio
#         video = editor.VideoFileClip("images.gif")
#         final_video = video.set_audio(audio).set_fps(24).resize(width=1280, height=720)

#         # Save the final video to the system's download folder
#         download_folder = os.path.expanduser("~/Downloads")  # Get the user's home directory
#         download_path = os.path.join(download_folder, "video.mp4")
#         final_video.write_videofile(fps=24, codec="libx264", filename=download_path)

#         # Serve the video as a downloadable response
#         with open(download_path, 'rb') as video_file:
#             response = HttpResponse(FileWrapper(video_file), content_type='video/mp4')
#             response['Content-Disposition'] = 'attachment; filename=video.mp4'
#             return response

#     return render(request, 'home.html')

def success_page(request):
    return render(request, 'success.html')


def home_page(request):
    if request.method == 'POST':
        audio_path = 'media/uploaded_audios/'
        images_path = 'media/uploaded_images/'
        os.makedirs(audio_path, exist_ok=True)
        os.makedirs(images_path, exist_ok=True)

        # Getting Input Audio File
        audio_file = request.FILES.get('audio')
        
        # Getting Input Images
        image_files = request.FILES.getlist('images')

        if audio_file:
            saved_audio_path = os.path.join(audio_path, audio_file.name)

            with open(saved_audio_path, 'wb') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)
                    
        for image_file in image_files:
            with open(os.path.join(images_path, image_file.name), 'wb') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

        # Use moviepy.AudioFileClip directly for Opus support
        saved_audio_file = os.path.join(audio_path, audio_file.name)
        audio = editor.AudioFileClip(saved_audio_file)
        audio_length = audio.duration

        list_of_images = []
        for image_file in sorted(os.listdir(images_path)):
            if image_file.endswith('.png') or image_file.endswith('.jpg'):
                image_path = os.path.join(images_path, image_file)
                # image = Image.open(image_path).resize((1280, int(720 * (Image.open(image_path).width / 1280))), Image.Resampling.LANCZOS)
                image = Image.open(image_path).resize((1280, 720), Image.Resampling.LANCZOS)
                print(f"Image: {image_file}, Dimensions: {image.size}")
                list_of_images.append(image)

        duration = audio_length / len(list_of_images)
        # imageio.mimsave('images.gif', list_of_images, fps=1/duration)
        gif_path = 'images.gif'
        list_of_images[0].save(
            gif_path,
            save_all=True,
            append_images=list_of_images[1:],
            duration=int(duration * 1000),  # duration is in milliseconds
            loop=0  # 0 means infinite loop
        )

        # Create video from GIF and set the audio
        video = editor.VideoFileClip("images.gif")
        final_video = video.set_audio(audio).set_fps(24)

        # Save the final video to the system's download folder
        download_folder = os.path.expanduser("~/Downloads")  # Get the user's home directory
        download_path = os.path.join(download_folder, "video.mp4")
        final_video.write_videofile(fps=24, codec="libx264", filename=download_path)

        # Serve the video as a downloadable response
        with open(download_path, 'rb') as video_file:
            response = HttpResponse(FileWrapper(video_file), content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename=video.mp4'
            shutil.rmtree(images_path)
            shutil.rmtree(audio_path)
            return response
    return render(request, 'home.html')