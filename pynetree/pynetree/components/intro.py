import pynecone as pc

def intro():
    return pc.text("""
                Welcome to my personal website! I'm a senior software engineer at Capital One
                and a part-time graduate computer science student at the Georgia Institute of Technology. I'm currently contributing to
                research in the field of edge cloud computing.
            """, 
                style=text_style
            )


text_style = {
    # "font_family": "Comic Sans MS",
    "font_size": "1.2em",
    "width": "50%",
    "textAlign": "center"
}