from flet import *
from list import List

def main(page:Page):
    page.window_width=400
    page.window_height=650
    page.update()
    page.add(List(page))
    page.scroll="auto"
    page.window_center()

if __name__=="__main__":
    app(main)