from src.userInterface.mainframe.graphicaluserinterface import GraphicalUserInterface

ROOT_TITLE: str = "Search Algorithm Visualization"
GEOMETRY_MEASUREMENT: str = "800x800"


def main():

    window = GraphicalUserInterface()
    window.title(ROOT_TITLE)
    window.geometry(GEOMETRY_MEASUREMENT)

    window.mainloop()


if __name__ == "__main__":
    main()
