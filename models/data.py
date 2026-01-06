from dataclasses import dataclass, field
from datetime import datetime
from errors import MissingNowError
from utils.formatters import format_stardust

    
@dataclass
class User:
    id: int
    username: str
    planet_id: int
    x: int
    y: int
    direction: int
    stardust: int
    created_at: datetime
    last_updated: int

@dataclass
class UserCount:
    user_id: int
    walk: int
    turn: int
    rocket: int
    kill: int
    post: int
    page: int
    book: int
    shelf: int
    planet: int
    special: int
    planet_draw: int
    user_draw: int

@dataclass
class Planet:
    id: int
    name: str
    width: int
    height: int
    created_name: str
    created_at: datetime

@dataclass(frozen=True)
class Tile:
    kind: str
    content: str = ""
    
@dataclass(frozen=True)
class NoneTile(Tile):
    kind: str = "none"
    content: str = "none"
    
@dataclass
class Object:
    id: int
    kind: str
    content: str
    good:int
    bad:int
    created_name:str
    created_at: datetime
    children: list["Object"] = field(default_factory=list)

@dataclass
class Surround:
    s4: Tile
    s5: Object | None
    s6: Tile
    s7: Tile
    s8: Tile
    s9: Tile
    
    
@dataclass
class ActionContext:
    cur: any
    session: dict
    db_now: datetime
    self_id: int | None