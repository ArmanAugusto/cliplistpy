#!/bin/python3

from rich.console import Console
from rich.syntax import Syntax

def title_header():
    console = Console()
    console.print(
        "\n\n\n\n\t[bold light_sky_blue1]***********************" +
        "******************[/]\n\n" +
        "\t[bold cornflower_blue]CLIP[/] : " + 
        "[bold cornflower_blue]C[/][light_sky_blue1]ommand[/] " + 
        "[bold cornflower_blue]L[/][light_sky_blue1]ine[/] " + 
        "[bold cornflower_blue]I[/][light_sky_blue1]tem[/] " + 
        "[bold cornflower_blue]P[/][light_sky_blue1]riorities[/]" +
        "[bold cornflower_blue]ListPy[/]\n\n" +
        "\t[bold light_sky_blue1]*********************************" +
        "********[/]\n\n")


def about_cliplistpy():
    console = Console()
    with open("about_cliplistpy.txt", "r") as file:
        text = file.read()

    syntax = Syntax(text, "text", theme="monokai", line_numbers=False)
    console.print(f"\n\n" + text + "\n\n")


def main_menu():
    console = Console()
    console.print(
        "\n\t\t[bold cornflower_blue]1[/] " +
        "- [bold light_sky_blue1]View Existing List[/]"
        "\n\t\t[bold cornflower_blue]2[/] " +
        "- [bold light_sky_blue1]Add Item[/]"
        "\n\t\t[bold cornflower_blue]3[/] " +
        "- [bold light_sky_blue1]Remove Item[/]"
        "\n\t\t[bold cornflower_blue]4[/] " +
        "- [bold light_sky_blue1]About CLIPListPy [/]\n\n")


def main_menu_actions():
    console = Console()
    choice = console.input(
        "\t\t    [light_sky_blue1]menu option:  [/]")

    # check validity of choice
    if choice.isnumeric() and int(choice) in range(0, 5):
        if choice == '1':
            print("\n\n\tThe priorities list with be viewed here\n\n")
        elif choice == '2':
            print("\n\n\tYou'll be able to add a new item here\n\n")
        elif choice == '3':
            print("\n\n\tYou'll be able to remove an item here\n\n")
        else:
            about_cliplistpy()
    else:
        print(f"\n\n\t\t{choice} is not a valid option from the menu\n\n")


if __name__=='__main__':
    title_header()
    main_menu()
    main_menu_actions()


