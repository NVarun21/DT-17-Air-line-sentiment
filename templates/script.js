document.getElementById('analyzeBtn').addEventListener('click', function() {
    const inputText = document.getElementById('sentimentInput').value;
    const resultDiv = document.getElementById('result');

    // Simple sentiment analysis logic (for demonstration purposes)
    const positiveWords = ['happy', 'good', 'great', 'excellent', 'awesome'];
    const negativeWords = ['sad', 'bad', 'terrible', 'awful', 'poor'];

    let positiveCount = 0;
    let negativeCount = 0;

    positiveWords.forEach(word => {
        if (inputText.toLowerCase().includes(word)) {
            positiveCount++;
        }
    });

    negativeWords.forEach(word => {
        if (inputText.toLowerCase().includes(word)) {
            negativeCount++;
        }
    });

    if (positiveCount > negativeCount) {
        resultDiv.textContent = 'Positive Sentiment 😊';
    } else if (negativeCount > positiveCount) {
        resultDiv.textContent = 'Negative Sentiment 😠';
    } else {
        resultDiv.textContent = 'Neutral Sentiment 😐';
    }
});