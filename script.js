document.getElementById('analyzeButton').addEventListener('click', function() {
    const text = document.getElementById('textInput').value;
    const lineCount = countLines(text);
    const wordCount = countWords(text);
    const consonantCount = countConsonants(text);
    const vowelCount = countVowels(text);
    const numberCount = countNumbers(text); // New line for number count
    
    document.getElementById('lineCount').textContent = `Line Count: ${lineCount}`;
    document.getElementById('wordCount').textContent = `Word Count: ${wordCount}`;
    document.getElementById('consonantCount').textContent = `Consonant Count: ${consonantCount}`;
    document.getElementById('vowelCount').textContent = `Vowel Count: ${vowelCount}`;
    document.getElementById('numberCount').textContent = `Number Count: ${numberCount}`; // New line for number count
});

document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const text = e.target.result;
            document.getElementById('textInput').value = text;
            document.getElementById('analyzeButton').click();  // Automatically analyze the uploaded file
        };
        reader.readAsText(file);
    }
});

function countLines(text) {
    return text.split(/\r\n|\r|\n/).length;
}

function countWords(text) {
    const words = text.trim().split(/\s+/);
    return words.length > 0 && words[0] !== '' ? words.length : 0;
}

function countConsonants(text) {
    const consonants = text.match(/[b-df-hj-np-tv-z]/gi);
    return consonants ? consonants.length : 0;
}

function countVowels(text) {
    const vowels = text.match(/[aeiou]/gi);
    return vowels ? vowels.length : 0;
}

function countNumbers(text) { // New function for number count
    const numbers = text.match(/\d+/g);
    return numbers ? numbers.length : 0;
}
