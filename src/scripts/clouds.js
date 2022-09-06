function importAll(r) {
    return r.keys().map(r);
}

function loadCloudImages() {
    const images = importAll(require.context('/public/assets/clouds/', false, /\.(png|jpe?g|svg)$/));

    let cloudImages = [];

    for (let i = 0; i < images.length; i++) {
        const cloudImage = new Image();
        cloudImage.src = images[i];
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

function initClouds() {
    const canvas = document.getElementById("canvas1");
    const ctx = canvas.getContext("2d");

    const CANVAS_WIDTH = canvas.width = 500;
    const CANVAS_HEIGHT = canvas.height = 1000;

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

export const runClouds = () => {
    initClouds();
}