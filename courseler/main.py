from helpers import Course, Menu


def main():

    #################################################################
    ###### DECLARE VARIABLES ######
    #################################################################
    main_menu = Menu()
    running = True
    options = {
        "1": "Enter a new Course Directory",
        "2": "Delete files",
        "3": "Find out video duration of the course",
        "4": "Create a torrent file of the course directory (WIP)"
    }
    menu_line = main_menu.create_menu(options)
    course = None
    course_dir = ""
    #################################################################

    while running:
        main_menu.display_menu(menu_line)

        user_input = input()

        if user_input == "1":
            # Get a course
            course_dir = input("Enter the course directory: ")
            course = Course(course_dir)

        elif user_input == "2":
            user_extensions = input(
                "Enter the type of files you want to delete: ")
            try:
                course.delete_files(user_extensions)
            except AttributeError:
                print("Course Directory is not yet declared.\n")

        elif user_input == "3":

            try:
                hour, minute, second = course.get_total_course_duration()
                print(
                    f"The total course duration is {hour}h {minute}min {second}sec.\n")
            except AttributeError:
                print("Course Directory is not yet declared.")

        elif user_input == "4":
            pass

        else:
            print("Please enter a valid option!")
            continue

    hour, minute, seconds = course.get_total_course_duration()
    # print(hour, minute, seconds)
    # print("Deleting Files right now.")
    # course.delete_files("srt")


if __name__ == '__main__':
    main()
