var message_input_ = document.getElementById(`message-input`);

message_input_.addEventListener('input', async () => {
    const text = message_input_.value;

    const response = await fetch('/count_tokens', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();
    const token_count = data.token_count;

    console.log(`Token count: ${token_count}`);
});
