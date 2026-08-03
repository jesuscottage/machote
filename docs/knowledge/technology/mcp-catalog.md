# Catálogo de Servidores MCP

> Última actualización: 2026-08-03
> **Ninguno está activo por defecto** — activa solo lo que necesites.
> Para activar: copia `.mcp.json.example` a `.mcp.json` y agrega los servidores.

---

## Notas importantes (2026)

- **Servidores remotos** son la tendencia: GitHub, Vercel, Stripe, Slack, Notion, Sentry ya ofrecen endpoints HTTP con OAuth. Preferir remotos cuando estén disponibles.
- **Optimización de tokens**: cada MCP inyecta 2,000–5,000 tokens al inicio. Regla de oro: **instalar 3, no 13**.
- **Servidores archivados**: Anthropic archivó 14 servidores de referencia (GitHub, Slack, PostgreSQL, Puppeteer, etc.). Siguen funcionando pero sin mantenimiento — preferir las versiones oficiales de cada vendor.
- **Seguridad**: solo el 8.5% de servidores públicos usa OAuth. Priorizar servidores oficiales.

---

## 1. Servidores de referencia (Anthropic)

Mantenidos por Anthropic. No requieren API key (excepto donde se indica).

| MCP | Comando | Qué hace | Cuándo activar |
|-----|---------|----------|----------------|
| **Filesystem** | `npx -y @modelcontextprotocol/server-filesystem /ruta` | Lectura/escritura de archivos con controles de acceso | Cuando Claude necesite acceso fuera del proyecto |
| **Memory** | `npx -y @modelcontextprotocol/server-memory` | Memoria persistente basada en knowledge graphs | Para contexto entre sesiones |
| **Sequential Thinking** | `npx -y @modelcontextprotocol/server-sequential-thinking` | Razonamiento paso a paso para problemas complejos | Decisiones de arquitectura, debugging |
| **Git** | `uvx mcp-server-git` | Operaciones Git locales (status, diff, commit, branch) | Cuando necesites operaciones Git avanzadas |
| **Fetch** | `npx -y @modelcontextprotocol/server-fetch` | Descarga y conversión de contenido web | Scraping básico, lectura de URLs |
| **Time** | `npx -y @modelcontextprotocol/server-time` | Conversión de tiempo y zonas horarias | Aplicaciones con zonas horarias |
| **Everything** | `npx -y @modelcontextprotocol/server-everything` | Servidor de prueba con todas las capacidades MCP | Testing y desarrollo de MCPs |

---

## 2. Desarrollo y documentación

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Context7** | `npx -y @upstash/context7-mcp@latest` | Documentación actualizada de librerías (React, Next.js, Prisma, etc.) | Opcional | **Siempre recomendado** para desarrollo |
| **Playwright** | `npx @playwright/mcp@latest --headless` | Automatización de navegador, E2E testing, screenshots | No | Scraping, testing, automatización web |
| **Desktop Commander** | `npx -y @wonderwhy-er/desktop-commander` | Shell, filesystem, procesos — ~25 herramientas | No | Operaciones avanzadas de sistema |
| **DeepWiki** | Remoto: `https://mcp.deepwiki.com/mcp` | Resúmenes wiki de repos GitHub públicos | No | Explorar repos desconocidos |
| **TaskMaster AI** | `npx -y task-master-ai@latest` | Gestión de tareas con IA, parsing de PRDs | No | Proyectos complejos con muchas tareas |

---

## 3. Integraciones AI/LLM

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Gemini** | `npx -y gemini-mcp-tool` | Integración con Google Gemini | `GEMINI_API_KEY` | Skills de revisión/consulta con Gemini |
| **Ollama** | `npx -y ollama-mcp` | Puente con modelos Ollama locales | No (Ollama local) | Modelos locales como reviewer |
| **Hugging Face** | `npx -y @huggingface/mcp-server` | Hub de HF: modelos, datasets, Spaces, papers | `HF_TOKEN` | ML/AI, exploración de modelos |
| **ElevenLabs** | `npx -y @elevenlabs/elevenlabs-mcp` | Text-to-speech, clonación de voz, transcripción | `ELEVENLABS_API_KEY` | Audio, podcasts, voiceovers |
| **OpenAI (Ask Codex)** | `npx -y ask-codex-mcp` | Consulta GPT/Codex como segundo reviewer | `OPENAI_API_KEY` | Revisión multi-modelo |

---

## 4. Bases de datos

### Relacionales

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **PostgreSQL** | `npx -y @modelcontextprotocol/server-postgres` | Conexión directa a PostgreSQL | Connection string | Debugging/consultas PostgreSQL |
| **Supabase** | `npx -y @supabase/mcp-server-supabase` | Queries, migraciones, auth, Edge Functions | `SUPABASE_ACCESS_TOKEN` | Proyectos con Supabase |
| **Neon** | Remoto: `https://mcp.neon.tech/mcp` | Postgres serverless con branching | OAuth | Proyectos con Neon |
| **MySQL** | `npx -y @modelcontextprotocol/server-mysql` | Conexión directa MySQL | Connection string | Proyectos con MySQL |
| **SQLite** | `npx -y @modelcontextprotocol/server-sqlite` | Base de datos SQLite local | Ruta del archivo | Proyectos con SQLite |

### NoSQL

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **MongoDB** | `npx -y @mongodb-js/mongodb-mcp-server` | ~39 herramientas: queries, esquema, embeddings | Connection string | Proyectos con MongoDB |
| **Redis** | `npx -y @modelcontextprotocol/server-redis` | Operaciones Redis: get/set, listas, hashes | No (Redis accesible) | Proyectos con Redis |
| **DuckDB** | `npx -y @motherduckdb/mcp-server-duckdb` | SQL analytics local | No | Análisis de datos local |
| **ClickHouse** | `npx -y @clickhouse/mcp-server` | Data warehouse en tiempo real | Credenciales | Analytics a escala |
| **Elasticsearch** | Docker: `elastic/mcp-server-elasticsearch` | Búsqueda y análisis de datos | Credenciales | Búsqueda full-text |

### Datos y analytics

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **BigQuery** | `npx -y @ergut/mcp-bigquery-server` | Read-only a BigQuery | Credenciales GCP | Proyectos con BigQuery |
| **Snowflake** | `pip install snowflake-labs-mcp` | NL-to-SQL, búsqueda semántica | Credenciales Snowflake | Data warehousing |
| **Airtable** | `npx -y airtable-mcp-server` | Lectura/escritura con inspección de schema | `AIRTABLE_API_KEY` | Bases de datos ligeras |

### Bases de datos vectoriales (RAG / memoria de agente)

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Qdrant** | `uvx mcp-server-qdrant` | Memoria semántica, modo embedded local | Opcional | RAG, memoria de agente |
| **ChromaDB** | `pip install chroma-mcp` | 13 herramientas, 4 modos de deploy | Opcional | RAG en desarrollo local |
| **Pinecone** | `npx -y @pinecone-database/mcp` | Búsqueda en cascada con reranking (solo cloud) | `PINECONE_API_KEY` | RAG en producción |
| **Milvus** | `pip install mcp-server-milvus` | 14 herramientas, búsqueda híbrida | Opcional | RAG con búsqueda híbrida |

---

## 5. Cloud y hosting

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **AWS** | `uvx awslabs.core-mcp-server@latest` | Servicios AWS completos | Credenciales AWS | Proyectos en AWS |
| **AWS Docs** | `uvx awslabs.aws-documentation-mcp-server@latest` | Documentación oficial de AWS | Credenciales AWS | Consulta rápida de docs AWS |
| **GCP** | Via `gcloud` CLI o servicio administrado | Cloud Storage, Compute, etc. | `gcloud auth` | Proyectos en GCP |
| **Azure** | Documentado en learn.microsoft.com | Servicios Azure completos | Credenciales Azure | Proyectos en Azure |
| **Azure DevOps** | GitHub: `microsoft/azure-devops-mcp` | Work items, repos, builds, wikis | PAT | Equipos con Azure DevOps |
| **Cloudflare** | `npx -y @cloudflare/mcp-server-cloudflare` | Workers, KV, R2, D1, DNS — 2,500+ endpoints | `CLOUDFLARE_API_TOKEN` | Proyectos en Cloudflare |
| **Vercel** | Remoto: `https://mcp.vercel.com` | Deployments, env vars, dominios | OAuth | Proyectos en Vercel |
| **Netlify** | GitHub: `netlify/netlify-mcp` | Deploy, sitios, extensions, logs | Token Netlify | Proyectos en Netlify |
| **DigitalOcean** | GitHub: `digitalocean-labs/mcp-digitalocean` | 16+ herramientas de gestión | Bearer token | Proyectos en DO |

---

## 6. DevOps e infraestructura como código

### Contenedores

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Docker** | GitHub: `ckreiling/mcp-server-docker` | Containers, imágenes, redes, volúmenes, Compose | No | Workflows con Docker |
| **Docker Gateway** | GitHub: `docker/mcp-gateway` | Gateway MCP con aislamiento de contenedores | No | MCP en contenedores |
| **Kubernetes** (Red Hat) | GitHub: `containers/kubernetes-mcp-server` | 40+ herramientas, nativo Go | kubeconfig | Clusters K8s |
| **Helm** | GitHub: `zekker6/mcp-helm` | Charts, repos, values, dependencias | Opcional | Gestión de Helm charts |

### IaC y GitOps

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Terraform** | `docker run -i --rm hashicorp/terraform-mcp-server` | Workspaces, runs, state, costos, registry | Token TF Cloud | Infraestructura con Terraform |
| **Pulumi** | GitHub: `pulumi/mcp-server` | Preview, up, outputs, code gen | Token Pulumi Cloud | Infraestructura con Pulumi |
| **ArgoCD** | `npx argocd-mcp@latest stdio` | Apps, recursos, clusters GitOps | `ARGOCD_API_TOKEN` | GitOps con ArgoCD |

---

## 7. CI/CD y control de versiones

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **GitHub** (remoto) | Remoto: `https://api.githubcopilot.com/mcp/` | 60+ herramientas: repos, PRs, issues, Actions | OAuth | Flujos avanzados de GitHub |
| **GitHub** (local) | `npx -y @modelcontextprotocol/server-github` | Mismo, versión local | `GITHUB_TOKEN` | Si no puedes usar el remoto |
| **GitLab** (oficial) | Documentado en docs.gitlab.com | Issues, MRs, pipelines | OAuth 2.0 | Equipos con GitLab |
| **GitLab** (comunidad) | GitHub: `zereight/gitlab-mcp` | MRs, issues, pipelines, wikis | Token | Alternativa más completa |
| **CircleCI** | GitHub: `CircleCI-Public/mcp-server-circleci` | Logs, jobs, pipelines, artifacts | `CIRCLECI_TOKEN` | CI con CircleCI |
| **Bitbucket** | `npx -y bitbucket-mcp` | Repos, PRs, pipelines | Credenciales | Equipos con Bitbucket |
| **Sourcegraph** | Remoto: `sourcegraph.com/mcp` | Code search con regex, filtros cross-repo | OAuth | Búsqueda en monorepos |

---

## 8. Monitoreo y observabilidad

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Sentry** | `npx -y @sentry/mcp-server` o remoto: `mcp.sentry.dev` | Errores, stack traces, performance | OAuth / `SENTRY_AUTH_TOKEN` | Monitoreo de errores |
| **Grafana** | `uvx mcp-grafana` | Prometheus, Loki, alertas, dashboards | `GRAFANA_SERVICE_ACCOUNT_TOKEN` | Dashboards y métricas |
| **Datadog** | Remoto en docs.datadoghq.com | 16+ herramientas: logs, metrics, APM | OAuth | Si usas Datadog |
| **New Relic** | Remoto: `mcp.newrelic.com/mcp/` | 35 herramientas: NRQL, alertas, logs | NR API key | Si usas New Relic |
| **PagerDuty** | Remoto: `mcp.pagerduty.com` | 60+ herramientas: incidentes | OAuth | Gestión de incidentes |
| **Prometheus** | `docker run mcp/server/prometheus` | Consultas PromQL, análisis de métricas | No (endpoint) | Métricas Prometheus |
| **Splunk** | Splunkbase app | SPL searches, knowledge objects | OAuth 2.1 | Si usas Splunk |

---

## 9. Calidad de código y testing

### Calidad

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **ESLint** | `npx @eslint/mcp@latest` | ESLint nativo como MCP | No | Proyectos JavaScript/TypeScript |
| **SonarQube** | GitHub: `SonarSource/sonarqube-mcp-server` | Métricas, issues, security hotspots, 20+ lenguajes | Token SonarQube | Análisis de calidad |
| **Semgrep** | Built into Semgrep CLI | SAST: código, supply chain, secrets | Sí | Seguridad de código |

### Testing

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Playwright** | `npx @playwright/mcp@latest --headless` | Automatización E2E, multi-browser | No | Testing E2E |
| **Vitest** | `npx @madrus/vitest-mcp-server` | Tests Vitest, cobertura, TDD | No | Proyectos con Vitest |

---

## 10. Navegador, scraping y búsqueda

### Scraping

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Firecrawl** | `npx -y firecrawl-mcp` o remoto: `https://mcp.firecrawl.dev/v2/mcp` | URLs a Markdown/JSON limpio | `FIRECRAWL_API_KEY` (opc.) | Web scraping estructurado |
| **Apify** | `npx -y @apify/actors-mcp-server` | Miles de scrapers pre-construidos | `APIFY_TOKEN` | Scraping a escala |
| **Crawl4AI** | `npx -y mcp-crawl4ai-ts` | Web crawler open-source | `CRAWL4AI_BASE_URL` | Crawling auto-hospedado |
| **Browserbase** | `npx -y @browserbase/mcp-server` | Anti-bot bypass, sesiones en la nube | `BROWSERBASE_API_KEY` | Sitios con protección anti-bot |

### Búsqueda

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Brave Search** | `npx -y @modelcontextprotocol/server-brave-search` | Búsqueda web via Brave | `BRAVE_API_KEY` | Búsqueda web general |
| **Exa** | `npx -y @anthropic/exa-mcp-server` | Búsqueda web semántica | `EXA_API_KEY` | Investigación profunda |
| **Tavily** | `npx -y tavily-mcp` | Búsqueda optimizada para AI | `TAVILY_API_KEY` | Alternativa a Brave |
| **Arxiv** | `npx -y arxiv-mcp-server` | Preprints académicos | No | Investigación ML/CS |

---

## 11. Comunicación y mensajería

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Slack** (local) | `npx -y @modelcontextprotocol/server-slack` | Mensajes, canales, DMs | `SLACK_BOT_TOKEN` | Notificaciones Slack |
| **Slack** (remoto) | Remoto: `mcp.slack.com` | Mismo, OAuth oficial | OAuth | Alternativa hospedada |
| **Discord** | `npx -y mcp-discord` | Servidores, canales, mensajes | `DISCORD_TOKEN` | Bots Discord |
| **Telegram** | `npx -y telegram-mcp` | Búsqueda de mensajes, gestión de chats | `TELEGRAM_API_ID/HASH` | Automatización Telegram |
| **WhatsApp** (Business) | `npx -y whatsapp-mcp-server` | Mensajes via WhatsApp Business API | Credenciales Meta | Comunicación empresarial |
| **Twilio** | Remoto: `mcp.twilio.com` | 1,400+ endpoints: SMS, voz, video | `TWILIO_ACCOUNT_SID` | SMS, voz, comunicaciones |
| **Microsoft Teams** | `npx -y outlook-mcp-server` | Email y mensajería via Graph API | MS Graph API | Equipos con Teams |

---

## 12. Email y marketing

### Email

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Gmail** | Built-in en Claude | Leer, enviar, gestionar emails | OAuth | Disponible via ToolSearch |
| **Resend** | `npx -y resend-mcp` | API completa: enviar, broadcasts, contactos | `RESEND_API_KEY` | Email transaccional moderno |
| **SendGrid** | GitHub: `deyikong/sendgrid-mcp` | 59 herramientas: campañas, contactos | `SENDGRID_API_KEY` | Email a escala |
| **Mailgun** | `npx -y @mailgun/mcp-server` | Email transaccional | `MAILGUN_API_KEY` | Alternativa a Resend |
| **Nylas** | `npx -y @nylas/cli` | 16 herramientas: Gmail, Outlook, IMAP | Nylas API key | Multi-proveedor de email |

### Marketing

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **HubSpot** | `npx -y @hubspot/mcp-server` o remoto: `mcp.hubspot.com` | CRM + marketing completo | `HUBSPOT_ACCESS_TOKEN` | Marketing + CRM integrado |
| **Mailchimp** | `npx -y @agentx-ai/mailchimp-mcp-server` | Campañas de email | `MAILCHIMP_API_KEY` | Email marketing |
| **Brevo** | `npx -y @houtini/brevo-mcp` | Email + SMS, A/B testing | `BREVO_API_KEY` | Marketing multi-canal |
| **ActiveCampaign** | Remoto: `mcp.activecampaign.com` | Workflows de automatización | API key | Automatización de marketing |
| **Klaviyo** | Remoto (GA) | Campañas, listas, reporting (e-commerce) | Klaviyo API Key | Marketing e-commerce |

---

## 13. Gestión de proyectos y productividad

### Gestión de proyectos

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Atlassian** (Jira + Confluence) | Remoto: `mcp.atlassian.com` | Jira, Confluence, Compass, Bitbucket | OAuth 2.1 | Equipos con Atlassian |
| **Atlassian** (comunidad) | `uvx mcp-atlassian` | 72 herramientas Jira + Confluence | API token | Alternativa local |
| **Linear** | `npx -y @linear/mcp-server` o remoto: `mcp.linear.app` | Issues, proyectos, ciclos, equipos | `LINEAR_API_KEY` | Equipos con Linear |
| **Notion** | `npx -y @notionhq/notion-mcp-server` | Páginas, bases de datos, bloques | `NOTION_TOKEN` | Documentación en Notion |
| **Asana** | `npx -y @roychri/mcp-server-asana` | Tareas, proyectos, workspaces | `ASANA_ACCESS_TOKEN` | Equipos con Asana |
| **ClickUp** | Remoto: `mcp.clickup.com/mcp` | ~49 herramientas: tareas, búsqueda | OAuth / API key | Equipos con ClickUp |
| **Monday.com** | `npx -y @mondaydotcomorg/monday-api-mcp` | Tableros, items, columnas | `MONDAY_TOKEN` | Equipos con Monday |
| **Trello** | `npx -y @hint-services/mcp-trello` | Tableros, listas, tarjetas | Trello API credentials | Tableros Kanban |
| **Todoist** | `npx -y @doist/todoist-mcp` | 44 herramientas de gestión de tareas | `TODOIST_API_TOKEN` | Gestión personal de tareas |

### Productividad

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Google Workspace** | `npx -y google-workspace-mcp` | Drive, Docs, Sheets, Calendar, Gmail | Google OAuth | Suite de Google |
| **Microsoft 365** | `npx -y @softeria/ms-365-mcp-server` | Office 365 via Graph API | MS Graph credentials | Suite de Microsoft |
| **Obsidian** | `npx -y @huangyihe/obsidian-mcp` | Leer, crear, actualizar notas en vault | No (ruta al vault) | Knowledge management personal |
| **Google Sheets** | `npx -y @akchro/google-sheets-mcp` | Leer, escribir, agregar datos | Google OAuth | Hojas de cálculo |

---

## 14. CRM y ventas

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Salesforce** | Remoto hospedado por Salesforce | 60+ herramientas, SOQL, objetos, informes | Salesforce OAuth | CRM enterprise |
| **HubSpot** | `npx -y @hubspot/mcp-server` | Contactos, empresas, deals, tickets | `HUBSPOT_ACCESS_TOKEN` | CRM + marketing |
| **Pipedrive** | `npx -y pipedrive-mcp` | 155 herramientas: deals, personas | `PIPEDRIVE_API_TOKEN` | CRM de ventas |
| **Attio** | `npx -y @attio/mcp-server` | CRM moderno, registros, listas | Attio API key | CRM alternativo |

---

## 15. Redes sociales y SEO

### Redes sociales

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **X/Twitter** | Remoto: `api.x.com/mcp` | Archivo completo, tendencias, bookmarks | X API credentials | Social media / monitoreo |
| **LinkedIn** | `npx -y linkedin-mcpserver` | Perfiles, búsqueda, mensajería | LinkedIn credentials | Networking profesional |
| **Ayrshare** | `npx -y @ayrshare/mcp` | 13+ plataformas, 75+ herramientas | Ayrshare API key | Social media multi-plataforma |
| **Postiz** | Auto-hospedado | Programación social, open-source (28k stars) | Auto-hospedado | Alternativa OSS a Buffer |

### SEO y analytics

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Google Search Console** | `npx -y mcp-gsc` | Rendimiento de búsqueda, 700+ stars | Google OAuth | SEO |
| **Ahrefs** | Remoto hospedado | Keyword difficulty, backlinks, tráfico | Ahrefs API key | Análisis SEO |
| **Semrush** | Remoto: `mcp.semrush.com` | Keywords, competidores, auditorías | OAuth | Análisis SEO completo |

---

## 16. Finanzas, pagos y e-commerce

### Pagos

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Stripe** | Remoto: `mcp.stripe.com` | Pagos, suscripciones, facturas, clientes | Stripe API key / OAuth | Pagos con tarjeta |
| **PayPal** | Remoto: `mcp.paypal.com` | Facturas, órdenes, disputas, suscripciones | PayPal OAuth | Pagos con PayPal |
| **QuickBooks** | `npm install quickbooks-online-mcp-server` | ~20 herramientas CRUD contables | OAuth 2.0 QuickBooks | Contabilidad |

### E-commerce

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Shopify** | 4 servidores oficiales (Storefront, Customer, Checkout, Dev) | Búsqueda semántica, carrito, colecciones | Shopify credentials | Tiendas Shopify |

---

## 17. CMS y contenido

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Contentful** | `npx -y @contentful/mcp-server` | Crear, editar, organizar, publicar contenido | `CONTENTFUL_MANAGEMENT_ACCESS_TOKEN` | CMS headless |
| **Sanity** | Remoto: `mcp.sanity.io` | Schema-aware, GROQ queries, OAuth | OAuth | CMS con Sanity |
| **WordPress** | `npx -y @aiondadotcom/mcp-wordpress` | Gestión completa del CMS | WordPress credentials | Sitios WordPress |

---

## 18. Diseño y creatividad

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Figma** | `npx -y figma-developer-mcp` | Diseños, tokens, variantes, Plugin API | `FIGMA_ACCESS_TOKEN` | Design-to-code |
| **Canva** | Built-in en Claude | Diseño gráfico, presentaciones | OAuth | Diseño rápido |
| **21st.dev** | `npx -y @21st-dev/magic-mcp` | Componentes UI generados con IA | `TWENTY_FIRST_API_KEY` | UI con IA |
| **DALL-E** | `npx -y mcp-image-generator` | Generación de imágenes con DALL-E 3 | `OPENAI_API_KEY` | Generación de imágenes |
| **Midjourney** | `npx -y mj-mcp` | Generación, variaciones, face swap | GPTNB API key | Imágenes estilizadas |

---

## 19. Calendario, traducción y reuniones

### Calendario

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Google Calendar** | `npx -y mcp-google-calendar` | Eventos, disponibilidad, zonas horarias | Google OAuth | Gestión de calendario |
| **Calendly** | Servidor MCP oficial | Disponibilidad, reservas, links | Calendly OAuth | Programación de citas |
| **Zoom** | `npx -y zoom-mcp-server` | Programación de reuniones | Zoom OAuth | Reuniones Zoom |
| **tl;dv** | `npx -y @tldv-public/tldv-mcp-server` | Inteligencia de reuniones (Meet, Zoom, Teams) | tl;dv credentials | Notas de reuniones automáticas |

### Traducción

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **DeepL** | `npx -y deepl-mcp-server` | Traducción, reformulación, detección | `DEEPL_API_KEY` | Traducción de calidad (500k char/mes gratis) |
| **Crowdin** | MCP oficial | Gestión de traducciones colaborativa | Crowdin API key | Localización de apps |
| **Lokalise** | MCP oficial | Plataforma de localización | Lokalise API key | i18n a escala |

---

## 20. Memoria y contexto persistente

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Memory** (Anthropic) | `npx -y @modelcontextprotocol/server-memory` | Knowledge graph local persistente | No | Memoria entre sesiones |
| **Mem0** | `npx @openmemory/install --client claude` | Memoria persistente cross-sesión y cross-cliente | `OPENMEMORY_API_KEY` | Memoria avanzada |
| **Omega Memory** | `npx -y @omega-memory/core` | #1 en LongMemEval benchmark | No | Memoria de largo plazo |
| **ConPort** | `npx -y context-portal-mcp` | Knowledge graph específico de proyecto | No | Contexto de proyecto |

---

## 21. Automatización y workflows

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **n8n** | Servidor MCP nativo | Construir, probar, publicar workflows | n8n credentials | Automatización con n8n |
| **Zapier** | `npx -y zapier-mcp` | Automatización multi-app | Zapier credentials | Integraciones rápidas |
| **Make** | `npx -y make-mcp` | Automatización visual | Make credentials | Workflows visuales |
| **Composio** | Remoto: endpoint único | 250+ integraciones (GitHub, Slack, Notion, Jira...) | Composio API key | Hub de integraciones |

---

## 22. Seguridad y autenticación

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Auth0** | `npx -y @auth0/auth0-mcp-server` | Management API via NL, crear apps, deploy Actions | OAuth interactivo | Autenticación con Auth0 |
| **Clerk** | Remoto (public beta) | SDK snippets, patrones de implementación | OAuth | Autenticación moderna |
| **Trivy** | GitHub: `aquasecurity/trivy-mcp` | Vulnerability scanning, misconfigs, secrets | Opcional | Auditoría de seguridad |
| **Prowler** | Remoto: `https://mcp.prowler.com/mcp` | Detecta misconfigs, genera PRs de remediación | Sí | Seguridad cloud |

---

## 23. APIs y desarrollo de APIs

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Postman** | Remoto: `mcp.postman.com` | 100+ herramientas: collections, environments | OAuth 2.0 | Desarrollo de APIs |
| **OpenAPI** | `npx -y @anthropic-ai/openapi-mcp-server` | Genera herramientas MCP desde specs OpenAPI 3.0+ | No | APIs documentadas con OpenAPI |
| **GraphQL** | `npx -y mcp-graphql` | Introspección dinámica de schemas GraphQL | No | APIs GraphQL |

---

## 24. Mapas y ubicación

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **Google Maps** | `npx -y @modelcontextprotocol/server-google-maps` | Geocoding, Places, Directions, Distance Matrix | `GOOGLE_MAPS_API_KEY` | Aplicaciones con mapas |
| **Mapbox** | `npx -y @mapbox/mcp-server` | Maps, Search, Geocoding, Directions, Isochrone | `MAPBOX_ACCESS_TOKEN` | Mapas personalizados |

---

## 25. Notificaciones

| MCP | Comando | Qué hace | API Key | Cuándo activar |
|-----|---------|----------|---------|----------------|
| **ntfy** | `npx -y ntfy-mcp-server` | Notificaciones push vía ntfy | No (o ntfy token) | Alertas self-hosted |
| **Desktop Notifications** | `npx -y mcp-notifier` | Notificaciones de escritorio cross-platform | No | Alertas locales |

---

## Recursos del ecosistema

| Recurso | URL | Descripción |
|---------|-----|-------------|
| Registro oficial | `registry.modelcontextprotocol.io` | API REST para descubrimiento de servidores |
| PulseMCP | `pulsemcp.com/servers` | Directorio comunitario, 22,000+ servidores |
| Awesome MCP (punkpeye) | `github.com/punkpeye/awesome-mcp-servers` | Lista curada más popular (91,800+ stars) |
| MCP.Directory | `mcp.directory` | 3,000+ servidores indexados |
| Docker Hub MCP | `hub.docker.com/u/mcp` | Catálogo de MCPs en Docker |
| Smithery CLI | `npx -y @smithery/cli install` | Instalador automático de MCPs |

---

## Cómo configurar

### 1. Copiar el archivo de ejemplo

```bash
cp .mcp.json.example .mcp.json
```

### 2. Editar `.mcp.json`

Agregar los servidores que necesites. Ejemplo con Context7 y Playwright:

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

Para servidores remotos (HTTP):

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

### 3. Variables de entorno

Algunos MCPs requieren API keys. Agregar a `.env.local`:

```bash
# Gemini MCP
GEMINI_API_KEY=tu_key

# Brave Search MCP
BRAVE_API_KEY=tu_key

# Sentry MCP
SENTRY_AUTH_TOKEN=tu_token

# Stripe MCP
STRIPE_SECRET_KEY=tu_key

# HubSpot MCP
HUBSPOT_ACCESS_TOKEN=tu_token
```

### 4. Reiniciar Claude Code

Los MCPs se cargan al inicio. Reiniciar después de cambiar `.mcp.json`.

---

## Tips

- **Empezar con 3 servidores máximo**: Context7 + Playwright + uno específico del proyecto
- **Context7 es casi siempre útil** para proyectos de desarrollo
- **Built-in MCPs** (Gmail, Canva) no necesitan configuración — disponibles via ToolSearch
- **Preferir servidores remotos** cuando estén disponibles (menos overhead, mejor mantenimiento)
- **Cada servidor consume contexto** — más activos = menos espacio para conversación
- **Empezar en read-only** para bases de datos y Kubernetes en producción
- **Auditar servidores** como cualquier dependencia — pinear versiones
