from src.userInterface.graphicaluserinterface import GraphicalUserInterface

ROOT_TITLE: str = "Search Algorithm Presentation"
GEOMETRY_MEASUREMENT: str = "800x800"


def main():

    window = GraphicalUserInterface()
    window.title(ROOT_TITLE)
    window.geometry(GEOMETRY_MEASUREMENT)

    window.mainloop()


if __name__ == "__main__":
    main()
