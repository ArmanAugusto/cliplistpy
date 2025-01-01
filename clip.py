#!/bin/python3

from rich.console import Console
from rich.syntax import Syntax

def title_header():
    console = Console()
    console.print(
        "\n\n\n\n[bold light_sky_blue1]***********************" +
        "****************[/]\n\n" +
        "  [bold cornflower_blue]CLIP[/] : " + 
        "[bold cornflower_blue]C[/][light_sky_blue1]ommand[/] " + 
        "[bold cornflower_blue]L[/][light_sky_blue1]ine[/] " + 
        "[bold cornflower_blue]I[/][light_sky_blue1]tem[/] " + 
        "[bold cornflower_blue]P[/][light_sky_blue1]riorities[/]\n\n" +
        "[bold light_sky_blue1]*********************************" +
        "******[/]\n\n")


def about_clip():
    console = Console()
    with open("about_clip.txt", "r") as file:
        text = file.read()

    #syntax = Syntax(text, "text", theme="monokai", line_numbers=False)
    console.print(text)


def main_menu():
    console = Console()
    console.print(
        "\n\t[bold cornflower_blue]1[/] " +
        "- [light_sky_blue1]About CLIP[/]\n\n")


def main_menu_actions():
    console = Console()
    choice = console.input(
        "    [light_sky_blue1]menu option:  [/]")

    # check validity of choice
    if choice.isnumeric() and int(choice) in range(0, 2):
        if choice == '1':
            about_clip()
    else:
        print(f"{choice} is not a valid option from the menu")


if __name__=='__main__':
    title_header()
    main_menu()
    main_menu_actions()


