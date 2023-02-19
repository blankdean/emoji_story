import pynecone as pc

def social_box(item: list[str]):
    name, url = item[0], item[1]
    return pc.box(
            pc.link(
                pc.image(src=f"/{name}.png", width = "48px", style=image_style),
                pc.text(name, style=text_style),
                href=url,
                color="rgb(107,99,246)",
                is_external=True,
                style=link_style
            ),
            style = box_style
            )

def socials():
    return pc.vstack(
        social_box(["Linkedin", "https://www.linkedin.com/in/blankdean/"]),
        social_box(["Twitter", 'https://twitter.com/CodeWithDean']),
        social_box(["Medium", 'https://medium.com/@blankdean'])
    )

box_style = {
    "bg":"#f5f5f5",
    "border_radius":"md",
    "width":"300px",
    "padding":"1",
    "justifyItems":"center"
}

link_style = {
    "display":"flex",
    "alignItems":"center",
    "position":"relative",
    "height": "50px"
}

image_style = {
    "position":"absolute",
    "left": 0
}

text_style = {
    "margin": "0 auto",
    "color": "rgb(20, 20, 20)"
}