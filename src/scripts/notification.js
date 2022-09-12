function showMessage(result, successMessage, errorMessage) {
    if (result) {
      if (successMessage) {
        this.$waveui.notify(successMessage, "success");
      }
    } else {
      if (errorMessage) {
        this.$waveui.notify(errorMessage, "error");
      }
    }
  }

export const notifications = {
    getLocations
}

