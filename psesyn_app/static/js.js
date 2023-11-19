document.getElementById('showPosters').addEventListener('click', function() {
    document.getElementById('poster').style.display = 'block';
    document.getElementById('article').style.display = 'none';
    document.getElementById('showArticles').style.background = 'none';
    this.style.backgroundColor = 'rgba(255, 165, 0, 0.1)';
});

document.getElementById('showArticles').addEventListener('click', function() {
    document.getElementById('poster').style.display = 'none';
    document.getElementById('article').style.display = 'block';
    document.getElementById('showPosters').style.background = 'none';
    this.style.backgroundColor = 'rgba(255, 165, 0, 0.1)';
});