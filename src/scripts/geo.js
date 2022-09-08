// function displayUserCoordinatesWillingly() {
//     navigator.geolocation.getCurrentPosition(this.showPosition, this.showError, { timeout: 5000 });
// }

// async function displayUserCoordinatesUnwillingly() {
//     let r = await apiExternal.getCoordinates();
//     this.showPosition({
//         coords: r
//     });
// }

// function emitCoordinates() {
//     if (this.canEmit) {
//         this.$emit('userCoordinates', this.lat, this.lon);
//     }
// }

// if (navigator.geolocation) {
//     displayUserCoordinatesWillingly();
// } else {
//     alert("Geolocation is not supported by this browser");
//     displayUserCoordinatesUnwillingly();
// }