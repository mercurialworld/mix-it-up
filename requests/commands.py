import sys
import httpx

from requests.models import DRMMapData

drm_route = "http://localhost:13337"

# rye run <script> [1/bsr] [2/requester]
bsr_code: str = sys.argv[1]
if len(sys.argv) > 2:
    requester: str = sys.argv[2] | ""

def add_song():
    httpx.post(f"{drm_route}/addSong/{bsr_code}?user={requester}")

def query_song():
    res = httpx.get(f"{drm_route}/query/{bsr_code}")

    if res.status_code == 200:
        res_map: DRMMapData = DRMMapData(**res.json())

        nps_njs_info = [f"{diff.notes_per_second:.2f} ({diff.note_jump_speed})" for diff in res_map.diffs]

        # this is the code of All Time
        # TODO: don't do this
        print(f"[{res_map.bsr_key}] [▲ {res_map.votes[0]} / ▼ {res_map.votes[1]} ({(res_map.rating * 100):.2f})] [{res_map.artist} - {res_map.title}{" (" + res_map.sub_title + ")" if res_map.sub_title else ""}] [{res_map.upload_time:%d %b %Y}] [◷ {f"{res_map.duration // 60}:{res_map.duration % 60}"}] [NPS (NJS) {" / ".join(nps_njs_info)}]")