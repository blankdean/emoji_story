from pcconfig import config
import pynecone as pc
from .components.projects import projects
from .components.socials import socials
from .components.skills import skills
from .components.intro import intro
from .components.state import BaseState


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
            intro(),
            pc.divider(),
            pc.heading("Skills", size="md"),
            skills(),
            pc.divider(),
            pc.heading("Projects", size="md"),
            projects(),
            pc.divider(),
            pc.heading("Links", size="md"),
            socials(),
            # pc.foreach(State.links, lambda item: link_box(item))
            style = page_style
        )
    )

page_style = {
  "padding-bottom": "80px"

}

# Add state and page to the app.
app = pc.App(state=BaseState)
app.add_page(
    index,
    title="Dean Portfolio",
    description="Dean's Developer Portfolio",
    image="/splash.png",
)
# app.add_page(about, route="/about")
app.compile()
