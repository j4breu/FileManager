"""Main way to start the application, with: python run.py"""

from filemanager import create_app

if __name__ == "__main__":
    file_manager = create_app()
    file_manager.mainloop()
