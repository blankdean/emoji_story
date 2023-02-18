"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

class State(pc.State):
    links: list[list[str]] = [
        ["Linkedin", "https://www.linkedin.com/in/blankdean/"],
        ["Twitter", 'https://twitter.com/CodeWithDean'],
        ["Medium", 'https://medium.com/@blankdean']
    ]


def link_box(item: list[list[str]]):
    name, url = item[0], item[1]
    return pc.link(
            # pc.button(pc.hstack(pc.image(src=f"/Linkedin.png"), pc.spacer(), pc.text(name))),
            pc.button(pc.text(name)),
            href=url,
            color="rgb(107,99,246)",
            is_external=True
            )

def project_box(item: list[list[str]]):
    return pc.box(height="15em", width="15em", bg="lightgreen"),

def about():
    return pc.text("About Page")


def index():
    return pc.center(
        pc.vstack(
            pc.divider(),
            pc.avatar(size="xl", src="prof1.jpg"),
            pc.heading("Dean Blank"),
            pc.text("Software Engineer | MSCS @ Georgia Tech"),
            pc.divider(),
            pc.heading("About", size="md"),
            pc.text("""
                Welcome to my personal website! I'm a software engineer and graduate computer science
                student at the Georgia Institute of Technology. I'm currently contributing to
                research in the field of edge cloud computing.
            """, style=text_style),
            pc.divider(),
            pc.heading("Side Projects", size="md"),
            pc.responsive_grid(
                pc.box(pc.vstack(pc.image(src="/topcard.png", width="600px", height="80%"),pc.divider(), pc.heading("TopCard Mobile", size="sm")), height="15em", width="15em"),
                pc.box(height="15em", width="15em", bg="lightblue"),
                pc.box(height="15em", width="15em", bg="purple"),
                columns=[1, 1, 3, 3, 3],
                spacing="4",
            ),
            pc.divider(),
            pc.heading("Social", size="md"),
            pc.foreach(State.links, lambda item: link_box(item))
        )
    )


text_style = {
    # "font_family": "Comic Sans MS",
    "font_size": "1.2em",
    "width": "50%",
    "textAlign": "center"
}

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(
    index,
    title="Dean Portfolio",
    description="Dean's Developer Portfolio",
    image="/splash.png",
)
# app.add_page(about, route="/about")
app.compile()
