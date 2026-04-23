// app.js

const timelineData = [
    {
        id: 'registration',
        date: 'Step 1: Months Before',
        title: 'Voter Registration',
        description: 'Ensure you are registered to vote at your current address before the deadline.',
        keywords: ['register', 'registration', 'sign up']
    },
    {
        id: 'research',
        date: 'Step 2: Weeks Before',
        title: 'Research Candidates',
        description: 'Learn about the candidates, their platforms, and any ballot measures.',
        keywords: ['research', 'candidates', 'platforms', 'ballot', 'measures']
    },
    {
        id: 'plan',
        date: 'Step 3: Days Before',
        title: 'Make a Plan',
        description: 'Decide if you will vote early, by mail, or in person on Election Day. Check your polling location.',
        keywords: ['plan', 'early voting', 'mail', 'absentee', 'location', 'where']
    },
    {
        id: 'vote',
        date: 'Step 4: Election Day',
        title: 'Cast Your Ballot',
        description: 'Bring necessary ID, go to your polling station, and cast your vote.',
        keywords: ['vote', 'day', 'cast', 'id', 'bring', 'station']
    },
    {
        id: 'results',
        date: 'Step 5: After Polls Close',
        title: 'Election Results',
        description: 'Votes are counted and results are certified by election officials.',
        keywords: ['results', 'counted', 'certified', 'who won']
    }
];

const responses = {
    'register': 'To register to vote, you typically need to visit your local election office website or a national portal like vote.gov. Deadlines vary by location!',
    'id': 'ID requirements vary wildly. Some places require a photo ID (like a driver\'s license), while others accept a utility bill or no ID at all if you are on the voter roll. Always check your local requirements.',
    'primary': 'A primary election is how political parties choose their candidates for the general election. You may need to be registered with a specific party to vote in their primary.',
    'where': 'You can find your polling location by checking your local election authority\'s website or looking at your voter registration card.',
    'mail': 'Voting by mail (or absentee voting) allows you to fill out your ballot at home and mail it in or drop it at a secure box. Make sure to request your ballot early!',
    'default': 'That\'s a great question! While I\'m a basic assistant, I recommend checking your local government or election commission website for the most accurate and up-to-date information.'
};

document.addEventListener('DOMContentLoaded', () => {
    renderTimeline();
    setupChat();
});

function renderTimeline() {
    const container = document.getElementById('election-timeline');
    
    timelineData.forEach((item, index) => {
        const div = document.createElement('div');
        div.className = 'timeline-item';
        if (index === 0) div.classList.add('active'); // First item active by default
        
        div.innerHTML = `
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <span class="timeline-date">${item.date}</span>
                <h3>${item.title}</h3>
                <p>${item.description}</p>
            </div>
        `;
        
        div.addEventListener('click', () => {
            document.querySelectorAll('.timeline-item').forEach(el => el.classList.remove('active'));
            div.classList.add('active');
            
            // Add context to chat
            addSystemMessage(`You selected <strong>${item.title}</strong>. ${item.description} Need more info?`);
        });
        
        container.appendChild(div);
    });
}

function setupChat() {
    const input = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    
    sendBtn.addEventListener('click', () => handleUserInput(input.value));
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleUserInput(input.value);
    });
}

function handleUserInput(text) {
    if (!text.trim()) return;
    
    const input = document.getElementById('chat-input');
    input.value = ''; // Clear input
    
    // Add user message
    const chatContainer = document.getElementById('chat-container');
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message user-message';
    msgDiv.textContent = text;
    chatContainer.appendChild(msgDiv);
    
    scrollToBottom();
    
    // Simulate thinking and respond
    setTimeout(() => {
        generateResponse(text);
    }, 600);
}

// Global function for chips
window.handleChipClick = function(text) {
    handleUserInput(text);
};

function generateResponse(text) {
    const lowerText = text.toLowerCase();
    let reply = responses.default;
    
    for (const [key, value] of Object.entries(responses)) {
        if (lowerText.includes(key)) {
            reply = value;
            break;
        }
    }
    
    addSystemMessage(reply);
}

function addSystemMessage(text) {
    const chatContainer = document.getElementById('chat-container');
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message system-message';
    msgDiv.innerHTML = text; // allow HTML like <strong>
    chatContainer.appendChild(msgDiv);
    
    scrollToBottom();
}

function scrollToBottom() {
    const chatContainer = document.getElementById('chat-container');
    chatContainer.scrollTop = chatContainer.scrollHeight;
}
