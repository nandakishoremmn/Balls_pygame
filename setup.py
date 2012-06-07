from distutils.core import setup
import py2exe

setup(
    version = "1.0",
    description = "Catch It!",
    name = "Catch It!",
    windows = [{"script":"main.py"}],
    data_files = [ (".", ["images/ball.png", "images/play.gif"]) ]
    )
