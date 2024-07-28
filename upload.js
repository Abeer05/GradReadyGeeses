
document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    // Using Axios to send the file to the server
    axios.post('http://localhost:8000/upload', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
    .then(response => {
        console.log('File uploaded successfully', response);
    })
    .catch(error => {
        console.error('Error uploading file', error);
    });
});