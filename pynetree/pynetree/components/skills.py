import pynecone as pc

def badge(skill: str):
     return pc.badge(
            f"{skill}", 
            variant="subtle", 
            color_scheme="green",
            border_width = 2,
            border_color="#29AB87",
            style=badge_style
        )


def skills():
    return pc.responsive_grid(
            badge("Distributed Systems"),
            badge("Network Automation"),
            badge("Cloud (AWS, Azure)"),
            badge("Big Data"),
            badge("Python"),
            badge("Spark SQL"),
            badge("C/C++"),
            badge("ReactJS"),
            badge("SwiftUI"),
            badge("HTML"),
            badge("CSS"),
            badge("Docker"),
            badge("Ansible"),
            badge("Jenkins"),
            badge("Github"),
            badge("Excel VBA"),
            columns=[1, 2, 3, 4],
            spacing="4"
        )

badge_style = {
     "text-align":"center"
}