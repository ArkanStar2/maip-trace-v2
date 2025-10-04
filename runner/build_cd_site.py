# Build C&D Lawn Service site using Webby Agent
import os
from webby_agent import build_site

cfg = dict(
    name="C&D Lawn Service",
    # This should be the folder where you keep hero.jpg and logo.svg
    images_src=os.path.expanduser("~/Documents/webbySites/c-d-lawn-service/images"),
    headline="C & D Lawn Service",
    tagline="Mowing • Edging • Cleanup",
    phone="(803) 361-0657",
    email="cdlawn@example.com",
    city="Lexington",
    state="SC",
    about=("We’re a family-run team serving Lexington and Columbia, South Carolina. "
           "We focus on straight lines, tight edges, and spotless clean-ups—treating "
           "every yard like it’s our own."),
    services=[
      {"title":"Mowing & Edging","desc":"Clean cuts, sharp edges, tidy beds."},
      {"title":"Bush & Hedge Shaping","desc":"Pruning and shaping for neat growth."},
      {"title":"Mulch & Bed Refresh","desc":"Weeds out, fresh mulch, crisp edges."},
      {"title":"Tree Limb Trim (Low)","desc":"Remove low-hanging limbs, tidy branches."},
      {"title":"Leaf & Debris Cleanups","desc":"Seasonal cleanups; spotless yards."},
      {"title":"Commercial Maintenance","desc":"Keep storefronts clean and welcoming."}
    ]
)

out = build_site(cfg)
print("C&D built at:", out)

