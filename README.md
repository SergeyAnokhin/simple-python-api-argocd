# simple-python-api-argocd

Простое FastAPI-приложение с деплоем в Kubernetes через ArgoCD.

## Первый запуск

Выполни эти шаги один раз перед первым `git push`:

1. **Создай репозиторий на GitHub** и запушь код:
   ```bash
   git remote add origin https://github.com/SergeyAnokhin/simple-python-api-argocd.git
   git push -u origin main
   ```

2. **Зарегистрируй ArgoCD Application** (один раз, с любой машины с доступом к кластеру):
   ```bash
   kubectl apply -f argocd-app.yaml
   ```

   После этого ArgoCD начнёт следить за папкой `k8s/` в ветке `main`.

## Рабочий процесс

```
редактируешь .py файлы  →  git push  →  GitHub Actions собирает образ
→  обновляет тег в k8s/deployment.yaml  →  ArgoCD видит изменение  →  деплоит
```

Каждый пуш в `main` автоматически:
- Собирает Docker-образ и пушит в GHCR с тегами `latest` и `sha-XXXXXXX`
- Обновляет `k8s/deployment.yaml` с точным SHA-тегом
- ArgoCD обнаруживает изменение манифеста и синхронизирует кластер

## Доступ к API

| URL | Описание |
|-----|----------|
| `http://192.168.1.31:30080` | Корень API — статус и версия |
| `http://192.168.1.31:30080/health` | Healthcheck (используется liveness probe) |
| `http://192.168.1.31:30080/items` | Список items |
| `http://192.168.1.31:30080/items/1` | Получить item по ID |

### Веб-интерфейс документации

| URL | Описание |
|-----|----------|
| `http://192.168.1.31:30080/docs` | **Swagger UI** — интерактивная документация, можно выполнять запросы прямо в браузере |
| `http://192.168.1.31:30080/redoc` | **ReDoc** — альтернативный UI в читабельном формате |

## Структура проекта

```
simple-python-api-argocd/
├── app/
│   ├── main.py              # FastAPI app
│   ├── requirements.txt
│   └── routers/
│       └── items.py         # /items эндпоинты
├── Dockerfile
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   └── service.yaml
├── .github/
│   └── workflows/
│       └── build-and-deploy.yaml
└── argocd-app.yaml          # применяется вручную один раз
```
