from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal

MapDiff = Literal["Easy", "Normal", "Hard", "Expert", "ExpertPlus"]

class DRMModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_pascal)


class DRMMapMods(DRMModel):
    noodle_extensions: bool
    chroma: bool
    mapping_extensions: bool
    cinema: bool


class DRMDiff(DRMModel):
    difficulty: MapDiff 
    characteristic: str # man idk what the characteristic strings are anymore
    note_jump_speed: float
    notes_per_second: float
    map_mods: DRMMapMods
    score_saber_stars: float
    beat_leader_stars: float


class DRMMapData(DRMModel):
    bsr_key: str
    hash: str
    user: str | None
    title: str
    sub_title: str
    artist: str
    mapper: str
    duration: int
    votes: list[int] # upvote, downvote
    rating: float
    upload_time: datetime # fuck you (datetimes your unix epoch)
    cover: str # url
    diffs: list[DRMDiff]


class DRMQueuePositionData(DRMModel):
    spot: int
    queue_item: DRMMapData


class DRMMessage(BaseModel): # note this is not a DRMModel for??? reasons??? talk to parrot about this
    message: str