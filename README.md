# Raindeer Social

AI-native social media management: brand intelligence, an agent pipeline that
turns a calendar slot into a reviewed draft, and human-in-the-loop scheduling
and publishing — built as a modular monolith, not a pile of microservices.

For the full system design, data model, agent pipeline, and issue roadmap,
see [`raindeer-social-blueprint.md`](./raindeer-social-blueprint.md). This
README covers what's here and how to get running; the blueprint covers why.

## System overview

Four backend domains, one repo:

| Path                | Responsibility |
|----------------------|----------------|
| `apps/api`           | FastAPI monolith — routers per domain (`/brands`, `/calendar`, `/posts`, `/agents`, `/publishing`, `/analytics`) |
| `packages/agents`     | LangGraph agent graphs (research, creative, generation, reviewer, onboarding) |
| `apps/web`            | Next.js frontend |
| `packages/schemas`    | Pydantic + Zod schemas, generated from one OpenAPI source of truth |
| `migrations`          | Alembic migrations for the Postgres schema |

**Stack:** Python 3.11 / FastAPI / SQLAlchemy + Alembic · LangGraph ·
PostgreSQL (Supabase) + pgvector · Redis + Celery · Next.js + TypeScript ·
Docker Compose for local dev.

## Getting started

Local dev environment setup (Python, Node, Postgres/pgvector, Docker, Redis)
is tracked as Issue #1 and will be documented here once it lands. In the
meantime, see the blueprint's Milestone 0 section for the target setup.

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for branch naming, PR process,
commit style, and the review rules before opening a PR. See
[`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) for how we expect people to
treat each other in issues and reviews.

## License

Proprietary — see [`LICENSE.md`](./LICENSE.md).
