import pynecone as pc

def project_box(item: list[str]):
    return pc.box(
                pc.link(
                        pc.vstack(
                            pc.image(src=f"/{item[1]}", style=image_style ),
                            pc.spacer(),
                            pc.heading(f"{item[0]}", size="sm"),
                            align="center"
                        ),
                    href=f"{item[2]}",
                    is_external=True),
                style=project_box_style
            )

def projects():
    return pc.responsive_grid(
            project_box(["Auto-Emailer", "emailer.png", "https://github.com/blankdean/auto_emailer"]),
            project_box(["TopCard Mobile", "topcard.png", "https://mytopcard.app/"]),
            project_box(["URL Aggregator", "url_aggregator.png", "https://github.com/blankdean/Company_URL_Aggregator"]),
            columns=[1, 2, 3],
            spacing="4"
            )
                
project_box_style = {
    "height":"10em", 
    "width":"15em", 
    "border_radius":"10px",
    "border_color":"#d3d3d3",
    "border_width":"thin",
    "padding": "0.5px",
    # "background-color": "#f2f2f2"
}   

image_style = {
    "width":"600px", 
    "height":"110px",
    "border-top-left-radius": "10px",
    "border-top-right-radius": "10px"
}