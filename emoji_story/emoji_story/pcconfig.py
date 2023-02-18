import pynecone as pc

config = pc.Config(
    app_name="emoji_story",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
