from courseler import helpers
import datetime


def main():
    course = helpers.Course('/Users/sebastianyii/Desktop/Courses/Complete Intro to Linux and the Command-Line')
    dirs = course.traverse_dir()
    total_time = 0
    for dir in dirs:
        video = course.get_video_obj(dir)
        total_time += course.get_video_duration(video, 2)

    time_format = str(datetime.timedelta(seconds=total_time))

    hour, min, seconds = time_format.split(':')
    seconds = int(float(seconds))

    print(f"The total time you need is about: {hour} hour, {min} minutes, {seconds} seconds")


if __name__ == '__main__':
    main()
