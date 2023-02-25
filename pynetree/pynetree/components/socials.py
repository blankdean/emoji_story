import pynecone as pc
from .state import BaseState

class CondState(BaseState):
    show: bool = False
    pin: str
    unlock_msg: str = "Enter pin to view resume."

    def change(self):
        self.show = not (self.show)

    @pc.var
    def handle(self):
        if self.pin == "1234":
            return pc.redirect("https://finance.yahoo.com")

    def redirect(self):
        if self.pin == "0208":
            self.unlock_msg = "Resume unlocked"
            return pc.redirect("https://drive.google.com/file/d/1-Ulwg2iDjMh4P2eMyTtRF3_pOxSpXSAp/view?usp=sharing")
        else:
            self.unlock_msg = "Incorrect pin to unlock resume."


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

def resume_box(item: list[str]):
    name, url = item[0], item[1]
    return pc.vstack(
            pc.box(
                pc.button(
                    pc.image(src=f"/{name}.png", width = "48px", style=image_style),
                    pc.text(name, style=text_style),
                    color="rgb(107,99,246)",
                    style=link_style,
                    on_click=CondState.change,
                    type="button",
                    is_full_width=True
                ),
                style = box_style
            ),
            pc.cond(
                CondState.show,
                pc.vstack(
                    pc.text(CondState.unlock_msg),
                    pc.box(
                        pc.pin_input(
                            length=4,
                            on_change=CondState.set_pin,
                            mask=True
                        )
                    ),
                    pc.button("Unlock", on_click=CondState.redirect)
                    ),
                pc.text("")
            ),

        )

def socials():
    return pc.vstack(
        social_box(["Linkedin", "https://www.linkedin.com/in/blankdean/"]),
        social_box(["Twitter", 'https://twitter.com/CodeWithDean']),
        social_box(["Medium", 'https://medium.com/@blankdean']),
        resume_box(["Resume", 'https://drive.google.com/file/d/10KnLpg5O8vDTQwTlKggvs_QvRem9a0O5/view?usp=sharing'])
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
