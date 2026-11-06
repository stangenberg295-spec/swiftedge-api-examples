// Print a live order flow snapshot from Swiftedge (free, no key). Node 18+.
//   node snapshot.mjs eth      markets: btc eth sol xrp gold silver oil us500 us100
const market = process.argv[2] || "btc";
const r = await fetch(`https://swiftedge.uk/api/v1/snapshot?market=${market}`, { headers: { "User-Agent": "swiftedge-example/1.0" } });
if (!r.ok) throw new Error(`HTTP ${r.status}`);
const d = await r.json();
console.log(`${d.name} ${d.instrument}: ${d.price_usd} USD (${d.updated})`);
for (const side of ["bids", "asks"]) {
  for (const w of (d.order_book_walls?.[side] || []).slice(0, 3)) {
    console.log(`  ${side.slice(0, -1).padEnd(4)} wall ${String(w.price).padStart(10)}  ${Math.round(w.size_usd).toLocaleString("en-US")} USD`);
  }
}
console.log("live heatmap:", d.links.live_heatmap);
console.log(d.attribution);
