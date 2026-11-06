"""Watch the largest order book walls near price for one market and print when they change (polls every 30 s).
    python walls_watch.py gold
"""
import json
import sys
import time
import urllib.request
market = sys.argv[1] if len(sys.argv) > 1 else "btc"
url = "https://swiftedge.uk/api/v1/snapshot?market=" + market
def walls():
    req = urllib.request.Request(url, headers={"User-Agent": "swiftedge-example/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        d = json.load(r)
    w = d.get("order_book_walls") or {}
    return d["price_usd"], {(s, x["price"]) for s in ("bids", "asks") for x in w.get(s, [])}
last = set()
while True:
    try:
        px, now = walls()
        for s, p in sorted(now - last):
            print(time.strftime("%H:%M:%S"), "new wall   ", s[:-1], p, " price", px)
        for s, p in sorted(last - now):
            print(time.strftime("%H:%M:%S"), "wall gone  ", s[:-1], p, " price", px)
        last = now
    except Exception as e:
        print("error:", e)
    time.sleep(30)
