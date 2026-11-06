# Swiftedge API & MCP examples
Free live order flow data for **Bitcoin, Ethereum, Solana, XRP, gold, silver, WTI oil, US 500 and US 100**:
price, today's range, the largest order book walls near price, resting liquidity, positioning levels, funding,
open interest and large trades - from [Swiftedge](https://swiftedge.uk), the free live order flow platform.
- **No key, no sign-up.** HTTPS + JSON.
- **REST:** `GET https://swiftedge.uk/api/v1/snapshot?market=btc` · `GET https://swiftedge.uk/api/v1/markets`
- **OpenAPI:** https://swiftedge.uk/api/v1/openapi.json
- **MCP server (remote, Streamable HTTP, no auth):** `https://swiftedge.uk/mcp` - listed in the official MCP registry as `uk.swiftedge/orderflow`
- **Docs:** https://swiftedge.uk/developers
- **Research you can cite:** https://swiftedge.uk/research
Markets: `btc`, `eth`, `sol`, `xrp`, `gold`, `silver`, `oil`, `us500`, `us100` (see `/api/v1/markets`).
Responses are cached for 15 seconds, so polling faster returns the same numbers. Free to use; please link to
https://swiftedge.uk when you show the data.
## Quick start
```bash
curl -s "https://swiftedge.uk/api/v1/snapshot?market=btc" | python -m json.tool
```
### Python
```bash
python python/snapshot.py btc
python python/walls_watch.py gold
```
### JavaScript (Node 18+)
```bash
node javascript/snapshot.mjs eth
```
## Use it from an AI assistant (MCP)
Tools: `list_markets` and `get_market_snapshot`.
| Client | How |
|---|---|
| Claude Code | `claude mcp add --transport http swiftedge https://swiftedge.uk/mcp` |
| Claude (desktop / web) | Settings -> Connectors -> Add custom connector -> URL `https://swiftedge.uk/mcp` |
| Claude Desktop (config file) | see [`mcp/claude_desktop_config.json`](mcp/claude_desktop_config.json) |
| Cursor | copy [`mcp/cursor-mcp.json`](mcp/cursor-mcp.json) to `.cursor/mcp.json` |
| VS Code | copy [`mcp/vscode-mcp.json`](mcp/vscode-mcp.json) to `.vscode/mcp.json` |
Then ask, for example: *"Where are the biggest order book walls on Bitcoin right now?"* or
*"Compare funding and open interest for gold and silver."*
## What the numbers are
Measured live by Swiftedge from the perpetual futures order book and trades. Positioning levels are estimates built from
part of each market's positions, not measurements and not a forecast. Nothing here is trading advice.
## License
The example code is MIT licensed (see `LICENSE`). The data is free to use with a link to https://swiftedge.uk.
