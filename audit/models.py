from dataclasses import dataclass, field

@dataclass
class Follower:
    login: str
    name: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
    followers: int | None = None
    following: int | None = None
    public_repos: int | None = None
    public_gists: int | None = None
    avatar_url: str | None = None
    bio: str | None = None 

    # Catch-all for unknown GitHub fields
    extra: dict = field(default_factory=dict)

    def __init__(self, **kwargs):
        self.login = kwargs.pop("login")
        self.name = kwargs.pop("name", None)
        self.created_at = kwargs.pop("created_at", None)
        self.updated_at = kwargs.pop("updated_at", None) 
        self.followers = kwargs.pop("followers", None)
        self.following = kwargs.pop("following", None)
        self.public_repos = kwargs.pop("public_repos", None)
        self.public_gists = kwargs.pop("public_gists", None)
        self.avatar_url = kwargs.pop("avatar_url", None)
        self.bio = kwargs.pop("bio", None) 

        # Store everything else
        self.extra = kwargs
