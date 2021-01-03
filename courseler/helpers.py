import cv2
from pathlib import Path
from tqdm import tqdm
import datetime


class Course:
    def __init__(self, course_dir):
        self.course_dir = course_dir

    def get_path_object(self):
        """
        Returns a path object
        """
        return Path(self.course_dir)

    @staticmethod
    def get_video_obj(video_dir):
        """
        Get a video Object
        """
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

    def traverse_dir(self, ext):
        """
        Returns a list of absolute path of directories
        - helper function
        :param ext: Extension of files
        """
        path = self.get_path_object()
        return [directory.absolute().as_posix() for directory in path.glob(f'**/*.{ext}')]

    def delete_files(self, file_type):
        """
        Delete Files of file types
        :param file_type: extension of a file
        """
        paths = self.get_path_object()
        for path in tqdm(paths.glob(f'**/*.{file_type}')):
            path.unlink()

    def get_total_course_duration(self):
        """
        Get the total course.
        Returns a tuple with the hour, minute and seconds
        """
        dirs = self.traverse_dir("mp4")
        total_time = 0
        for directory in dirs:
            video = self.get_video_obj(directory)
            total_time += self.get_video_duration(video, 2)

        time_format = str(datetime.timedelta(seconds=total_time))

        hour, minute, seconds = time_format.split(':')
        seconds = int(float(seconds))

        return (hour, minute, seconds)


class Menu(object):
    """
    A Flexible Menu
    """

    def __init__(self):
        pass

    def create_menu(self, options: dict):
        """
        This function creates a menu. It takes in a dictionary and output
        """
        menu = ""
        for key, value in options.items():
            menu += f"{key}. {value}\n"

        return menu

    def display_menu(self, menu_line):
        """
        Accepts a formatted string of the menu and print it out
        """
        print(menu_line)
