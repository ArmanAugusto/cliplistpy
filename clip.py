#!/bin/python3

from rich.console import Console

def title_header():
    console = Console()
    console.print(
        "\n\n\t\t[bold light_sky_blue1]***********************" +
        "***************************[/]\n\n" +
        "\t\t\t[bold cornflower_blue]CLIP[/] : " + 
        "[bold cornflower_blue]C[/][light_sky_blue1]ommand[/] " + 
        "[bold cornflower_blue]L[/][light_sky_blue1]ine[/] " + 
        "[bold cornflower_blue]I[/][light_sky_blue1]tem[/] " + 
        "[bold cornflower_blue]P[/][light_sky_blue1]riorities[/]\n\n" +
        "\t\t[bold light_sky_blue1]*********************************" +
        "*****************[/]\n\n")


def main_menu():
    console = Console()
    console.print(
        "\n\n\t\t\t[bold cornflower_blue]1[/] " +
        "- [light_sky_blue1]About CLIP[/]\n\n")

if __name__=='__main__':
    title_header()
    main_menu()
