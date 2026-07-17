const storyboard = document.getElementById("storyboard");

storyboard.innerHTML = "";

scenes.forEach(scene => {

    storyboard.innerHTML += `

        <div class="card mb-3">

            <div class="card-body">

                <h4>Scene ${scene.scene}</h4>

                <h5>${scene.title}</h5>

                <p>${scene.description}</p>

                <small>${scene.duration} sec</small>

            </div>

        </div>

    `;

});