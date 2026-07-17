 document.addEventListener("DOMContentLoaded", () => {

    const generateBtn = document.getElementById("generateBtn");
    const generateSceneBtn = document.getElementById("generateSceneBtn");
    const generateImageBtn = document.getElementById("generateImageBtn");
    const generateVoiceBtn = document.getElementById("generateVoiceBtn");
    const audioList = document.getElementById("audioList");

    const storyOutput = document.getElementById("storyOutput");
    const storyboard = document.getElementById("storyboard");
    const imageGallery = document.getElementById("imageGallery");
    const generateVideoBtn = document.getElementById("generateVideoBtn");
    const videoOutput = document.getElementById("videoOutput");

    // ==========================================
    // Generate Story
    // ==========================================

    generateBtn.addEventListener("click", async () => {

        const projectName = document.getElementById("project_name").value.trim();
        const prompt = document.getElementById("prompt").value.trim();

        if (!projectName || !prompt) {
            alert("Please enter Project Name and Prompt.");
            return;
        }

        storyOutput.innerHTML = `
            <div class="alert alert-info">
                ⏳ Generating story...
            </div>
        `;

        storyboard.innerHTML = "";
        imageGallery.innerHTML = "";

        generateSceneBtn.disabled = true;
        generateImageBtn.disabled = true;
        generateVoiceBtn.disabled = true;
        generateVideoBtn.disabled = true;

        try {

            const response = await fetch("/generate-story", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    project_name: projectName,
                    prompt: prompt

                })

            });

            const data = await response.json();

            storyOutput.innerHTML = `
                <div class="card shadow">

                    <div class="card-body">

                        <h4>📖 Generated Story</h4>

                        <p style="white-space: pre-wrap;">
                            ${data.story}
                        </p>

                    </div>

                </div>
            `;

            generateSceneBtn.disabled = false;

        }

        catch (error) {

            console.error(error);

            storyOutput.innerHTML = `
                <div class="alert alert-danger">
                    Failed to generate story.
                </div>
            `;

        }

    });

    // ==========================================
    // Generate Scenes
    // ==========================================

    generateSceneBtn.addEventListener("click", async () => {

        const projectName = document.getElementById("project_name").value.trim();

        storyboard.innerHTML = `
            <div class="alert alert-info">
                ⏳ Generating scenes...
            </div>
        `;

        imageGallery.innerHTML = "";

        generateImageBtn.disabled = true;

        try {

            const response = await fetch("/generate-scenes", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    project_name: projectName

                })

            });

            const scenes = await response.json();

            storyboard.innerHTML = "";

            scenes.forEach(scene => {

                storyboard.innerHTML += `

                <div class="card mb-3 shadow-sm">

                    <div class="card-body">

                        <h4>🎬 Scene ${scene.scene}</h4>

                        <h5>${scene.title}</h5>

                        <p>${scene.description}</p>

                        <span class="badge bg-primary">

                            ${scene.duration} sec

                        </span>

                    </div>

                </div>

                `;

            });

            generateImageBtn.disabled = false;

        }

        catch (error) {

            console.error(error);

            storyboard.innerHTML = `
                <div class="alert alert-danger">
                    Failed to generate scenes.
                </div>
            `;

        }

    });

    // ==========================================
    // Generate Images
    // ==========================================

    generateImageBtn.addEventListener("click", async () => {

    const projectName = document.getElementById("project_name").value.trim();

    imageGallery.innerHTML = `
        <div class="alert alert-info">
            🖼 Generating images...
            <br><br>
            Please wait...
        </div>
    `;

    try {

        const response = await fetch("/generate-images", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                project_name: projectName

            })

        });

        const images = await response.json();

        imageGallery.innerHTML = "";

        images.forEach(image => {

            imageGallery.innerHTML += `

            <div class="col-md-4 mb-4">

                <div class="card shadow">

                    <img
                        src="/projects/${projectName}/images/${image}"
                        class="card-img-top"
                        style="height:300px; object-fit:cover;"
                    >

                    <div class="card-body">

                        <h6 class="text-center">

                            ${image}

                        </h6>

                    </div>

                </div>

            </div>

            `;

        });
        generateVoiceBtn.disabled = false;

    }

    catch(error){

        console.error(error);

        imageGallery.innerHTML = `

        <div class="alert alert-danger">

            Failed to generate images.

        </div>

        `;

    }
    });

    // ==========================================
// Generate Voice
// ==========================================

generateVoiceBtn.addEventListener("click", async () => {

    const projectName = document.getElementById("project_name").value.trim();

    audioList.innerHTML = `
        <div class="alert alert-info">
            🎙 Generating voice...
            <br><br>
            Please wait...
        </div>
    `;

    try {

        const response = await fetch("/generate-voice", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                project_name: projectName
            })

        });

        const audioFiles = await response.json();

        audioList.innerHTML = "";

        audioFiles.forEach(audio => {

            audioList.innerHTML += `

                <div class="card mb-3 shadow">

                    <div class="card-body">

                        <h5>${audio}</h5>

                        <audio controls style="width:100%;">

                            <source
                                src="/projects/${projectName}/audio/${audio}"
                                type="audio/mpeg">

                        </audio>

                    </div>

                </div>

            `;

        });
        generateVideoBtn.disabled = false;

    }

    catch(error){

        console.error(error);

        audioList.innerHTML = `
            <div class="alert alert-danger">
                Failed to generate voice.
            </div>
        `;

    }

});

// ==========================================
// Generate Video
// ==========================================

generateVideoBtn.addEventListener("click", async () => {

    const projectName = document.getElementById("project_name").value.trim();

    videoOutput.innerHTML = `
        <div class="alert alert-info">
            🎥 Generating Video...
            <br><br>
            Please wait...
        </div>
    `;

    try {

        const response = await fetch("/generate-video", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                project_name: projectName

            })

        });

        const data = await response.json();

        videoOutput.innerHTML = `

            <video
                controls
                width="100%">

                <source
                    src="/projects/${projectName}/video/${data.video}"
                    type="video/mp4">

            </video>

            <br><br>

            <a
                href="/projects/${projectName}/video/${data.video}"
                class="btn btn-success"
                download>

                ⬇ Download Video

            </a>

        `;

    }

    catch(error){

        console.error(error);

        videoOutput.innerHTML = `
            <div class="alert alert-danger">
                Failed to generate video.
            </div>
        `;

    }

});
});