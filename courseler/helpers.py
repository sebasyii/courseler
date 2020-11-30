import cv2
from pathlib import *


class Course(object):
    def __init__(self, course_dir):
        self.course_dir = course_dir

    def get_path_object(self):
        return Path(self.course_dir)

    @staticmethod
    def get_video_obj(video_dir):
        return cv2.VideoCapture(video_dir)

    @staticmethod
    def get_width(video):
        """
        Get the Width of the Video Frame
        :param video: cv2.VideoCapture Type Object
        :return: Float on the width of the Video
        """
        return video.get(cv2.CAP_PROP_FRAME_WIDTH)

    @staticmethod
    def get_height(video):
        """
        Get the height of the video frame
        :param video: cv2.VideoCapture Type Object
        :return: Float on the height of the Video
        """
        return video.get(cv2.CAP_PROP_FRAME_HEIGHT)

    @staticmethod
    def get_video_duration(video, decimal_places):
        """
        Get the video Duration of the the video
        :param video: cv2.VideoCapture Object
        :param decimal_places: Integer on how many decimal places you want
        :return: a float on the video duration
        """
        frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
        frames_per_sec = video.get(cv2.CAP_PROP_FPS)
        video_duration = round((frame_count / frames_per_sec), decimal_places)
        return video_duration

    def traverse_dir(self):
        path = self.get_path_object()
        return [dir.absolute().as_posix() for dir in path.glob('**/*.mp4')]

    def delete_files(self, file_type):
        paths = self.get_path_object()
        for path in paths.glob(f'**/*.{file_type}'):
            path.unlink()
