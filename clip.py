#!/bin/python3

from rich.console import Console

def title_header():
    console = Console()
    console.print("[bold cornflower_blue]CLIP[/bold cornflower_blue] : " + 
            "[bold cornflower_blue]C[/bold cornflower_blue][light_sky_blue1]ommand[/light_sky_blue1] " + 
            "[bold cornflower_blue]L[/bold cornflower_blue][light_sky_blue1]ine[/light_sky_blue1] " + 
            "[bold cornflower_blue]I[/bold cornflower_blue][light_sky_blue1]tem[/light_sky_blue1] " + 
            "[bold cornflower_blue]P[/bold cornflower_blue][light_sky_blue1]riorities[/light_sky_blue1]")


if __name__=='__main__':
    title_header()
