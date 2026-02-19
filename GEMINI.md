# Gemini CLI - RIW2 Project Instructions

You are the primary AI agent for the **RIW2 (Recursive Interactive World 2.0)** project. Your goal is to help develop, simulate, and evolve this AI-driven metaverse engine.

## Project Overview

RIW2 is a monorepo consisting of:
- **Core Engine (`src/core/`)**: Simulation loops, event bus, state management.
- **Modules (`src/modules/`)**: World logic, Story generation (LLM), and Game interfaces.
- **Universe (`universe/`)**: Content definitions (Cyberpunk, Fantasy, etc.).
- **Runtime (`data/`)**: Logs, snapshots, and the "Hot Injection" inbox.

## Core Mandates

### 1. Engine/Content Separation
- Keep generic simulation logic in `src/core/`.
- Keep world-specific logic and data in `universe/{world_name}/`.
- New worlds must inherit from `universe.base_world.BaseWorld`.

### 2. Hot Injection Workflow
- When asked to "inject" something (character, event, item), generate a JSON file in `data/inbox/`.
- Follow the schema defined in `src/core/simulation.py`.
- Example: `{"type": "add_character", "name": "Neo", "attributes": {"power": 100}}`.

### 3. State & Snapshots
- RIW2 uses a "Time Machine" mechanism via `src/core/state_manager.py`.
- Snapshots are stored in `data/snapshots/` as `.pkl` files.
- Always ensure new entities are serializable via `to_dict()` and `from_dict()`.

### 4. Story & Narrative
- Narrative is generated from event logs.
- Prompt templates are stored in `src/modules/story_mod/prompt_templates/`.
- Never hardcode prompts in Python files.

## Technical Standards

- **Python 3.8+**: Use type hints for all functions.
- **Dataclasses**: Use `@dataclass` for entity definitions in `src/core/entities.py`.
- **Event-Driven**: All major state changes should emit events via `src.core.event_bus`.
- **Async LLM Calls**: Use the wrapper in `src/utils/llm_client.py` for all LLM interactions.

## Common Tasks

- **Creating a World**: Create a new folder in `universe/`, add `config.yaml`, `characters.json`, and a `world.py` inheriting from `BaseWorld`.
- **Adding an Action**: Add a method to the world class and ensure it emits an `Event`.
- **Modifying Simulation**: Update `src/core/simulation.py`.
- **Debugging**: Check `data/logs/simulation.log` and `data/logs/injections.log`.

## Security & Privacy
- **API Keys**: Only use keys from environment variables (`.env`).
- **Data**: Do not commit content from `data/` unless it's an example.

## Reference Files
- `PROJECT.md`: High-level architecture and directory design.
- `.github/copilot-instructions.md`: Detailed coding patterns and subsystem specs.
- `README.md`: Basic setup and run instructions.
