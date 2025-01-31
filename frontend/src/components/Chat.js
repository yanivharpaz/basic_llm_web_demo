import React, { useState } from 'react';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = input;
    setInput('');
    setMessages(prev => [...prev, { text: userMessage, isUser: true }]);
    setIsLoading(true);

    try {
      console.log('Sending request to backend...');
      const response = await fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
      });

      const data = await response.json();
      console.log('Received response:', data);

      if (data.error) {
        console.error('Error from API:', data.error);
        setMessages(prev => [...prev, { text: `Error: ${data.error}`, isUser: false }]);
      } else {
        setMessages(prev => [...prev, { text: data.response, isUser: false }]);
      }
    } catch (error) {
      console.error('Network error:', error);
      setMessages(prev => [...prev, { text: 'Error: Could not get response from server', isUser: false }]);
    }

    setIsLoading(false);
  };

  return (
    <div className="chat-container">
      <div className="messages">
        {messages.length === 0 ? (
          <div className="message bot">Start a conversation...</div>
        ) : (
          messages.map((message, index) => (
            <div key={index} className={`message ${message.isUser ? 'user' : 'bot'}`}>
              <strong>{message.isUser ? 'You: ' : 'AI: '}</strong>
              {message.text}
            </div>
          ))
        )}
        {isLoading && <div className="message bot">AI is thinking...</div>}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading || !input.trim()}>
          {isLoading ? 'Sending...' : 'Send'}
        </button>
      </form>
    </div>
  );
}

export default Chat;
