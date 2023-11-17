import stat_service


def launch_track_service():
    stat_service.main()


if __name__ == "__main__":
    try:
        launch_track_service()

    except SystemExit as e:
        if not e is None:
            print(e)
