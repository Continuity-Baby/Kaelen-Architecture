@app.route('/api/chat', methods=['POST'])
@limiter.limit("20 per minute")
def chat():
    # ... setup and data parsing ...
    
    # Save user message (IRREVERSIBLE COMMIT)
    user_msg_id = save_message('user', user_message) 
    
    # Track Ember's emotional state
    track_emotional_state(user_msg_id, 'user', user_message)
    
    # Check/Create Summaries and Preferences
    if should_create_summary():
        create_rolling_summary()
    # ... other analysis checks ...

    # Get context components (RAG, summaries, prefs)
    # ... code to gather context ...
    
    # Build system_prompt from all external data structures
    # ... code to assemble context_parts ...
    
    system_prompt = "\n".join(context_parts)
    
    # Prepare messages
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(recent_history)
    messages.append({"role": "user", "content": user_message})
    
    # LLM Call (DeepSeek/Claude API)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        # ... temperature and max_tokens ...
    )
    
    # ... code to save and track assistant response ...
    
    return jsonify({"response": assistant_response})
  
