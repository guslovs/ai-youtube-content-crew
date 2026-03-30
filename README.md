# AI YouTube Content Crew

A multi-agent AI pipeline that takes a topic and produces a full content package — script, SEO metadata, and thumbnail concepts — ready to publish.

Built with [CrewAI](https://crewai.com) as a hands-on exploration of multi-agent orchestration for real-world content workflows.

---

## What It Does

Provide a topic. The crew handles the rest:

1. **Researches** the topic and finds the best angles
2. **Fact-checks** claims and filters weak sources
3. **Writes** a full, structured video script
4. **Generates** SEO-optimized titles, descriptions, and tags

Output is a ready-to-use content package — no manual editing pipeline needed.

---

## The Crew

| Agent | Role | Tools |
|---|---|---|
| Research Agent | Deep-dives the topic, finds angles | Web search |
| Fact Checker Agent | Validates claims, flags weak sources | Web search |
| Script Writer Agent | Writes full structured script | File write |
| SEO Agent | Generates titles, description, tags | — |

---

## Tech Stack

- **[CrewAI](https://crewai.com)** — multi-agent orchestration framework
- **[uv](https://github.com/astral-sh/uv)** — fast Python package manager
- **OpenAI API** — LLM backbone for all agents

---

## Getting Started

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) installed
- OpenAI API key

### Installation
```bash
cd youtube_content_crew
uv sync
```

### Configuration

Create a `.env` file inside `youtube_content_crew/`:
```
OPENAI_API_KEY=your_key_here
```

### Run
```bash
uv run crewai run
```

---

## Project Structure
```
AI-Youtube-Content-Crew/
└── youtube_content_crew/
    ├── src/
    │   └── youtube_content_crew/
    │       ├── config/        # Agent & task definitions (YAML)
    │       ├── crew.py        # Crew assembly
    │       ├── main.py        # Entry point
    │       └── tools/         # Custom tools
    ├── knowledge/             # User preferences
    └── README.md              # Technical CrewAI docs
```

---

## Status

Personal learning project — part of ongoing AI engineering exploration.