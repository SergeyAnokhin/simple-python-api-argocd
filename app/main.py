from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers import items

tags_metadata = [
    {
        "name": "general",
        "description": "Общие эндпоинты: статус сервиса и healthcheck.",
    },
    {
        "name": "items",
        "description": "Операции с объектами **Item**.",
    },
]

app = FastAPI(
    title="simple-python-api-argocd",
    version="1.1.0",
    description=(
        "Демо-приложение на **FastAPI**, задеплоенное в K3s через ArgoCD.\n\n"
        "Образ собирается автоматически GitHub Actions и публикуется в GHCR."
    ),
    openapi_tags=tags_metadata,
    docs_url=None,   # отключаем встроенный — используем тёмный ниже
    redoc_url=None,  # то же самое для ReDoc
)

app.include_router(items.router, prefix="/items", tags=["items"])


@app.get("/", tags=["general"], summary="Статус сервиса")
def root():
    """Возвращает текущий статус и версию сервиса."""
    return {"status": "ok", "version": "1.0.0"}


@app.get("/health", tags=["general"], summary="Healthcheck")
def health():
    """Используется Kubernetes liveness probe."""
    return {"healthy": True}


# ─────────────────────────────────────────────
#   Dark theme CSS for Swagger UI
# ─────────────────────────────────────────────
_SWAGGER_DARK_CSS = """
body { margin: 0; background: #111 !important; }
.swagger-ui { background: #111 !important; }

/* Top bar */
.swagger-ui .topbar { background: #1a1a1a; border-bottom: 1px solid #2e2e2e; }
.swagger-ui .topbar a { color: #cccccc; }

/* Info section */
.swagger-ui .info .title,
.swagger-ui .info hgroup .title { color: #eeeeee; }
.swagger-ui .info p, .swagger-ui .info li { color: #bbbbbb; }
.swagger-ui .info a { color: #7ab3f5; }
.swagger-ui .info code { background: #222; color: #e0e0e0; }

/* Scheme / servers bar */
.swagger-ui .scheme-container {
  background: #1a1a1a;
  box-shadow: none;
  border-bottom: 1px solid #2e2e2e;
}
.swagger-ui .servers-title { color: #cccccc; }
.swagger-ui .servers > label select { background: #222; color: #eee; border: 1px solid #444; }

/* Operation tags */
.swagger-ui .opblock-tag { color: #eeeeee; border-bottom: 1px solid #2e2e2e; }
.swagger-ui .opblock-tag:hover { background: #1e1e1e; }
.swagger-ui .opblock-tag small { color: #888888; }

/* Operation blocks */
.swagger-ui .opblock {
  background: #1a1a1a !important;
  border: 1px solid #2e2e2e !important;
  box-shadow: none !important;
}
.swagger-ui .opblock .opblock-summary { border-bottom: 1px solid #2e2e2e; }
.swagger-ui .opblock .opblock-summary-path { color: #eeeeee; }
.swagger-ui .opblock .opblock-summary-description { color: #aaaaaa; }
.swagger-ui .opblock .opblock-summary-operation-id { color: #888888; }
.swagger-ui .opblock-body { background: #1e1e1e; }
.swagger-ui .opblock-description-wrapper p { color: #bbbbbb; }

/* HTTP method badges */
.swagger-ui .opblock.opblock-get    .opblock-summary-method { background: #1b4a6b; }
.swagger-ui .opblock.opblock-post   .opblock-summary-method { background: #1b5e2e; }
.swagger-ui .opblock.opblock-put    .opblock-summary-method { background: #5e3a0b; }
.swagger-ui .opblock.opblock-delete .opblock-summary-method { background: #6b1f1f; }
.swagger-ui .opblock.opblock-patch  .opblock-summary-method { background: #3a3a00; }

/* Parameters table */
.swagger-ui table thead tr td,
.swagger-ui table thead tr th { color: #cccccc; border-bottom: 1px solid #333; }
.swagger-ui table tbody tr td { border-bottom: 1px solid #222; }
.swagger-ui .parameter__name { color: #eeeeee; }
.swagger-ui .parameter__type { color: #999999; }
.swagger-ui .parameter__in   { color: #666666; }
.swagger-ui .parameters-col_description p { color: #bbbbbb; }

/* Form inputs */
.swagger-ui input[type=text],
.swagger-ui input[type=password],
.swagger-ui input[type=search],
.swagger-ui input[type=email],
.swagger-ui textarea,
.swagger-ui select { background: #252525; color: #eeeeee; border: 1px solid #444; }
.swagger-ui input:focus, .swagger-ui textarea:focus { border-color: #666; outline: none; }

/* Buttons */
.swagger-ui .btn { background: #252525; color: #eee; border: 1px solid #555; }
.swagger-ui .btn:hover { background: #333; }
.swagger-ui .btn.execute     { background: #1a4a7a; border-color: #2a6aaa; color: #fff; }
.swagger-ui .btn.execute:hover { background: #1e5a8e; }
.swagger-ui .btn.cancel      { background: #5a1a1a; border-color: #8a2a2a; color: #fff; }
.swagger-ui .btn.authorize   { background: #1a4a1a; border-color: #2a7a2a; color: #7de27d; }

/* Responses */
.swagger-ui .responses-inner h4,
.swagger-ui .responses-inner h5 { color: #dddddd; }
.swagger-ui .response-col_status { color: #eeeeee; }
.swagger-ui .response-col_description { color: #bbbbbb; }

/* Code / pre */
.swagger-ui .highlight-code { background: #0d0d0d; }
.swagger-ui .highlight-code > .microlight { background: #0d0d0d; color: #e0e0e0; }
.swagger-ui pre.version { background: #0d0d0d; color: #e0e0e0; }
.swagger-ui code { background: #1e1e1e; color: #e0e0e0; }

/* Models */
.swagger-ui section.models { background: #1a1a1a; border: 1px solid #2e2e2e; }
.swagger-ui section.models h4 { color: #eeeeee; border-bottom: 1px solid #2e2e2e; }
.swagger-ui section.models .model-container { background: #1e1e1e; border: 1px solid #2e2e2e; }
.swagger-ui .model { color: #cccccc; }
.swagger-ui .model-title { color: #eeeeee; }
.swagger-ui .prop-type   { color: #7ab3f5; }
.swagger-ui .prop-format { color: #888888; }

/* Markdown */
.swagger-ui .markdown p, .swagger-ui .markdown li { color: #bbbbbb; }
.swagger-ui .markdown code { background: #222; color: #e0e0e0; }

/* Auth modal */
.swagger-ui .dialog-ux .backdrop-ux { background: rgba(0,0,0,.75); }
.swagger-ui .dialog-ux .modal-ux { background: #1e1e1e; border: 1px solid #444; }
.swagger-ui .dialog-ux .modal-ux-header { background: #1a1a1a; border-bottom: 1px solid #333; }
.swagger-ui .dialog-ux .modal-ux-header h3 { color: #eeeeee; }
.swagger-ui .dialog-ux .modal-ux-content p,
.swagger-ui .dialog-ux .modal-ux-content h4 { color: #cccccc; }

/* Custom scrollbar */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: #1a1a1a; }
::-webkit-scrollbar-thumb { background: #444; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #555; }
"""


@app.get("/docs", include_in_schema=False)
async def swagger_dark():
    """Swagger UI с тёмной темой."""
    html = f"""<!DOCTYPE html>
<html>
<head>
  <title>{app.title}</title>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
  <style>{_SWAGGER_DARK_CSS}</style>
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    SwaggerUIBundle({{
      url: "/openapi.json",
      dom_id: "#swagger-ui",
      presets: [SwaggerUIBundle.presets.apis, SwaggerUIBundle.SwaggerUIStandalonePreset],
      layout: "BaseLayout",
      deepLinking: true,
    }})
  </script>
</body>
</html>"""
    return HTMLResponse(html)


@app.get("/redoc", include_in_schema=False)
async def redoc_dark():
    """ReDoc с тёмной темой."""
    html = f"""<!DOCTYPE html>
<html>
<head>
  <title>{app.title} — ReDoc</title>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {{ margin: 0; padding: 0; background: #111111; }}
    ::-webkit-scrollbar {{ width: 8px; }}
    ::-webkit-scrollbar-track {{ background: #1a1a1a; }}
    ::-webkit-scrollbar-thumb {{ background: #444; border-radius: 4px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #555; }}
  </style>
</head>
<body>
  <div id="redoc-container"></div>
  <script src="https://cdn.jsdelivr.net/npm/redoc@latest/bundles/redoc.standalone.js"></script>
  <script>
    Redoc.init("/openapi.json", {{
      theme: {{
        colors: {{
          primary: {{ main: "#6ec5ff" }},
          text: {{ primary: "#e0e0e0", secondary: "#a0a0a0" }},
          border: {{ dark: "#333333", light: "#2e2e2e" }},
        }},
        sidebar: {{
          backgroundColor: "#1a1a1a",
          textColor: "#dddddd",
          activeTextColor: "#6ec5ff",
        }},
        rightPanel: {{
          backgroundColor: "#0d0d0d",
          textColor: "#eeeeee",
        }},
        typography: {{
          fontSize: "14px",
          fontFamily: "Roboto, sans-serif",
          code: {{
            backgroundColor: "#1e1e1e",
            color: "#e0e0e0",
          }},
          links: {{ color: "#7ab3f5" }},
        }},
      }},
    }}, document.getElementById("redoc-container"))
  </script>
</body>
</html>"""
    return HTMLResponse(html)
