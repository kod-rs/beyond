function loadCloudImages() {
    let cloudImages = [];
    let cloudCount = 20;
    let cloudPrefix = "../../../public/assets/clouds/Cloud_";
    let cloudSufix = ".png";

    for (let i = 1; i < cloudCount + 1; i++) {
        const cloudImage = new Image();
        cloudImage.src = cloudPrefix + String(i) + cloudSufix;
        cloudImages.push(cloudImage);
    }
    return cloudImages;
}


class Cloud {
    constructor(ctx, canvas, cloudImages) {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.width = 100;
        this.height = 100;
        this.speed = Math.random() * 4 - 2;
        this.image = cloudImages[5];
        this.image = cloudImages[Math.floor(Math.random() * 20)];
        this.ctx = ctx;
    }

    update() {
        this.x += this.speed;
        this.y += this.speed;
    }

    draw() {
        this.ctx.drawImage(this.image, this.x, this.y);
    }
}

function generateClouds(numberOfClouds, ctx, canvas) {
    const clouds = [];

    let cloudImages = loadCloudImages();

    for (let i = 0; i < numberOfClouds; i++) {
        clouds.push(new Cloud(ctx, canvas, cloudImages));
    }

    return clouds
}

window.onload = function () {

    const canvas = document.getElementById("canvas1");
    const ctx = canvas.getContext("2d");

    CANVAS_WIDTH = canvas.width = 500;
    CANVAS_HEIGHT = canvas.height = 1000;

    const numberOfClouds = 100;

    let clouds = generateClouds(numberOfClouds, ctx, canvas);

    function animate() {
        ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

        clouds.forEach(i => {
            i.update();
            i.draw();
        });

        requestAnimationFrame(animate);
    }

    animate();

}
