function previewPost() {
    var fileInput = document.getElementById("post-image");
    var file = fileInput.files[0];

    var captionInput = document.getElementById("post-caption");
    var caption = captionInput.value;

    console.log("File:", file);
    console.log("Caption:", caption);

    var formDiv = document.getElementById('form-div');

    if (file || caption.trim() !== '') {
        // Show the preview section
        console.log("Displaying preview section");
        document.getElementById('preview-container').style.display = 'block';
        formDiv.className = "w-50 border p-3 shadow col-6 bg-light";
    } else {
        // Hide the preview section
        console.log("Hiding preview section");
        document.getElementById('preview-container').style.display = 'none';
        formDiv.className = "w-100 border p-3 shadow col-6 bg-light";
    }

    if (file) {
        var reader = new FileReader();

        // Set up the FileReader to load the image as a data URL
        reader.onload = function (e) {
            // Update the image source with the data URL
            var imagePreview = document.getElementById('preview-image');
            imagePreview.src = e.target.result;
        };

        // Read the selected file as a data URL
        reader.readAsDataURL(file);
    }

    // Update the caption text
    var captionPreview = document.getElementById('preview-caption');
    captionPreview.textContent = caption;
}
