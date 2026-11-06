"""Print a live order flow snapshot from Swiftedge (free, no key).
    python snapshot.py btc        markets: btc eth sol xrp gold silver oil us500 us100
"""
import json
import sys
import urllib.request
market = sys.argv[1] if len(sys.argv) > 1 else "btc"
url = "https://swiftedge.uk/api/v1/snapshot?market=" + market
req = urllib.request.Request(url, headers={"User-Agent": "swiftedge-example/1.0"})
with urllib.request.urlopen(req, timeout=20) as r:
    d = json.load(r)
print("%s  %s  price %s USD  (%s)" % (d["name"], d["instrument"], d["price_usd"], d["updated"]))
t = d.get("today_utc") or {}
print("today (UTC): open %s  high %s  low %s  change %s %%" % (t.get("open"), t.get("high"), t.get("low"), t.get("change_pct")))
w = d.get("order_book_walls") or {}
for side in ("bids", "asks"):
    for x in w.get(side, [])[:3]:
        print("  %-4s wall %12s  %14s USD" % (side[:-1], x["price"], format(round(x["size_usd"]), ",")))
print("live heatmap:", d["links"]["live_heatmap"])
print(d.get("attribution", ""))
