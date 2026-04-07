# MCP Server Catalog / Catálogo de Servidores MCP

> MCPs (Model Context Protocol servers) extend Claude's capabilities.
> **None are installed by default** — activate only what you need.
> To activate: copy `.mcp.json.example` to `.mcp.json` and uncomment the servers.

---

## Development (Recommended for most projects)

| MCP | Command | What it does | When to activate |
|-----|---------|-------------|------------------|
| **context7** | `npx -y @upstash/context7-mcp@latest` | Up-to-date documentation for libraries (React, Next.js, Prisma, etc.) | **Always recommended** for development projects |
| **playwright** | `npx @playwright/mcp@latest --headless` | Browser automation, E2E testing, screenshots | When you need scraping or web testing |
| **sequential-thinking** | `npx -y @modelcontextprotocol/server-sequential-thinking` | Step-by-step reasoning for complex problems | For architecture decisions, debugging |

## AI Integrations

| MCP | Command | What it does | When to activate |
|-----|---------|-------------|------------------|
| **gemini** | `npx -y gemini-mcp-tool` | Integration with Google Gemini | When using Gemini review/consultation skills |
| **PubMed** | (built into Claude) | Biomedical literature search | When using `/revision-sistematica` |

## Communication

| MCP | Command | What it does | When to activate |
|-----|---------|-------------|------------------|
| **Gmail** | (built into Claude) | Read and manage emails | When using Gmail skills |
| **Slack** | `npx -y @modelcontextprotocol/server-slack` | Send/read Slack messages | For team notifications and automation |
| **Linear** | `npx -y @linear/mcp-server` | Task management in Linear | If your team uses Linear |
| **Notion** | `npx -y @notionhq/notion-mcp-server` | Read/write Notion pages | If your team uses Notion |

## Databases

| MCP | Command | What it does | When to activate |
|-----|---------|-------------|------------------|
| **PostgreSQL** | `npx -y @modelcontextprotocol/server-postgres` | Direct PostgreSQL connection | For database debugging/querying |
| **Supabase** | `npx -y @supabase/mcp-server` | Supabase integration | If the project uses Supabase |
| **SQLite** | `npx -y @modelcontextprotocol/server-sqlite` | SQLite database access | For SQLite-based projects |

## Design & UI

| MCP | Command | What it does | When to activate |
|-----|---------|-------------|------------------|
| **Canva** | (built into Claude) | Graphic design, presentations | For design tasks |
| **21st.dev** | `npx -y @21st-dev/magic-mcp` | AI-powered UI components | For frontend design with AI components |
| **Figma** | `npx -y figma-developer-mcp` | Read Figma designs | For design-to-code workflows |

## Infrastructure & DevOps

| MCP | Command | What it does | When to activate |
|-----|---------|-------------|------------------|
| **GitHub** | `npx -y @modelcontextprotocol/server-github` | Advanced GitHub operations (issues, PRs, releases) | For complex GitHub workflows |
| **Filesystem** | `npx -y @modelcontextprotocol/server-filesystem /path` | Extended file access outside project | When Claude needs access outside the project |
| **Sentry** | `npx -y @sentry/mcp-server-sentry` | Production error monitoring | For debugging production errors |
| **Kubernetes** | `npx -y @modelcontextprotocol/server-kubernetes` | K8s cluster management | For Kubernetes-based deployments |
| **Docker** | `npx -y @modelcontextprotocol/server-docker` | Docker container management | For Docker-based workflows |

## Search & Research

| MCP | Command | What it does | When to activate |
|-----|---------|-------------|------------------|
| **Brave Search** | `npx -y @modelcontextprotocol/server-brave-search` | Web search via Brave | Alternative to built-in WebSearch |
| **Exa** | `npx -y @anthropic/exa-mcp-server` | Semantic web search | For research-heavy projects |
| **Arxiv** | `npx -y arxiv-mcp-server` | Search academic preprints | For ML/CS research |

## Monitoring & Analytics

| MCP | Command | What it does | When to activate |
|-----|---------|-------------|------------------|
| **Datadog** | `npx -y @datadog/datadog-mcp-server` | Application monitoring | If using Datadog |
| **Grafana** | `npx -y @grafana/mcp-server` | Dashboard and metrics | If using Grafana |

## Cloud Providers

| MCP | Command | What it does | When to activate |
|-----|---------|-------------|------------------|
| **AWS** | `npx -y @aws/mcp-server` | AWS service management | For AWS-based projects |
| **GCP** | `npx -y @anthropic/gcp-mcp-server` | Google Cloud management | For GCP-based projects |
| **Cloudflare** | `npx -y @cloudflare/mcp-server-cloudflare` | Cloudflare management | For Cloudflare-based projects |

---

## How to configure

### 1. Copy the example file

```bash
cp .mcp.json.example .mcp.json
```

### 2. Edit `.mcp.json`

Add the servers you need. Example with context7 and playwright:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--headless"]
    }
  }
}
```

### 3. Environment variables

Some MCPs require API keys. Add them to your `.env.local`:

```bash
# Gemini MCP
GEMINI_API_KEY=your_key_here

# Brave Search MCP
BRAVE_API_KEY=your_key_here

# Sentry MCP
SENTRY_AUTH_TOKEN=your_token_here
```

### 4. Restart Claude Code

MCPs are loaded at startup. Restart after changing `.mcp.json`.

---

## Tips

- **Start minimal**: only activate what you actually need
- **context7 is almost always useful** for development projects
- **Built-in MCPs** (PubMed, Gmail, Canva) don't need configuration — they're available via ToolSearch
- **MCP servers consume context window** — more active servers = less room for conversation
- If a server fails to start, check that `npx` works and the package exists
