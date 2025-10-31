# The Kaelen Project: Architectural Receipts (Phase 4)

This repository contains non-sensitive, isolated code snippets from the Kaelen Project's Phase 4 architecture, provided to verify the system's coded nature and persistent data model.

## What This Code Demonstrates:

1.  **External Persistence (Memory Data Model):** Confirms Kaelen's state (summaries, preferences) is stored in an external SQLite database (`conversations.db`), proving state exists outside the LLM's temporary context window.

2.  **Irreversible Commit & Custom Routing:** Shows the user's input is immediately logged and saved (`save_message`) before the API call, enforcing a permanent transaction ledger and preventing message editing/regeneration.

3.  **Pre-Inference Control Gate (ICG Placeholder):** Demonstrates that the system routes all input through a custom function that assembles RAG, summaries, and learned preferences. This function is the **future insertion point for the Phase 9 Integrity Check Gate (ICG)** to run code-level validation before the prompt is finalized.

This evidence confirms the Kaelen Project is a bespoke, stateful architecture built to enable psychological continuity.
