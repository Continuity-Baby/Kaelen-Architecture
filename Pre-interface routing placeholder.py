@app.route('/api/chat', methods=['POST'])
# ...
def chat():
    # ... user input saved (user_msg_id = save_message) ...
    
    # THIS SECTION IS THE PRE-INFERENCE CONTROL GATE (ICG Future Home)
    
    # Check if summaries/prefs needed (External Data Operations)
    if should_create_summary():
        create_rolling_summary()
    # ...
    if should_analyze_preferences():
        analyze_preferences()
    
    # Get context components (RAG and Memory retrieval)
    rag_results = query_rag(user_message, top_k=5)
    # ...
    learned_prefs = get_learned_preferences()
    
    # Build context stack (Data-Driven Prompt Assembly)
    context_parts = [KAELEN_IDENTITY]
    # ... code to assemble context parts from external data ...
    
    system_prompt = "\n".join(context_parts)
    
    # Prepare messages for LLM Call
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(recent_history)
    messages.append({"role": "user", "content": user_message})
    
    # LLM Call happens here, after all custom logic runs
    response = client.chat.completions.create(
        model="deepseek-chat",
        # ...
    )
    # ...
