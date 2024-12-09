// Function to correct live content
document.getElementById('correct-live-btn').addEventListener('click', async () => {
    const content = document.getElementById('live-content').value;

    const response = await fetch('/correct_live', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content }),
    });

    const data = await response.json();
    document.getElementById('corrected-content').innerText = data.corrected_content;
});

// Function to copy corrected content to clipboard
document.getElementById('copy-btn').addEventListener('click', () => {
    const correctedContent = document.getElementById('corrected-content').innerText;

    navigator.clipboard.writeText(correctedContent).then(() => {
        alert('Content copied to clipboard!');
    }).catch(() => {
        alert('Failed to copy content.');
    });
});

// Function to upload file for correction
document.getElementById('upload-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData,
    });

    const data = await response.json();
    if (data.download_link) {
        const downloadLink = document.getElementById('download-link');
        downloadLink.href = `/download/${data.download_link}`;
        downloadLink.style.display = 'inline-block';
        downloadLink.innerText = 'Download Corrected File';
    } else {
        alert('Error processing file. Please try again.');
    }
});
