def get_learned_preferences():
    """Get learned preferences about Ember"""
    conn = sqlite3.connect('conversations.db') # Connects to external DB
    c = conn.cursor()
    c.execute('SELECT category, preference_text, confidence_score, context_tags FROM learned_preferences WHERE confidence_score > 0.5 ORDER BY last_updated DESC LIMIT 10')
    prefs = c.fetchall()
    conn.close()
    
    if not prefs:
        return ""
    
    pref_text = "\n\nLEARNED PATTERNS (for context, not rules):\n"
    # ... code to format preferences for context ...
    
    return pref_text
  
