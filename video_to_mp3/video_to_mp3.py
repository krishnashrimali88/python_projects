import subprocess
import imageio_ffmpeg

def convertor(input_file,output_file):
    ff_path =  imageio_ffmpeg.get_ffmpeg_exe()

    ffmpeg_cmd = [
        ff_path,
        "-i",input_file,
        "-vn",
        "-acodec","libmp3lame",
        "-ab","192k",
        "-ar","44100",
        "-y",
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd,check=True)
        print("successfully converted")
    except subprocess.CalledProcessError as e:
        print("conversion failed")



convertor("python.mp4","my.mp3")
