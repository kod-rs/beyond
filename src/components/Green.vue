<template>

    <div v-show="timerCount !== 0">
        <div class="alert alert-success" role="alert">
            {{ this.content }} {{ timerCount }}
        </div>
    </div>

</template>
  

  <script>
  
  export default {
      name: "GreenBanner",
      props: {
          customContent: String,
          //   countdown: Number
      },
      data() {
          return {
              content: this.customContent,
              //   timerCount: this.countdown,
              timerCount: 0
          }
      },
  
      methods: {
          setContent(content) {
              this.content = content
          },
          show() {
              this.timerCount = 3;
          }
      },
  
      watch: {
  
          timerCount: {
              handler(value) {
  
                  if (value > 0) {
                      setTimeout(() => {
                          this.timerCount--;
                      }, 1000);
                  }
  
              },
              immediate: true
          },
          // countdown: function (newVal, oldVal) {
          //     //   if (newVal == 0) {
          //     //       this.timerCount = 0
  
          //     //       return
          //     //   }
          //     console.log('Prop changed: ', newVal, ' | was: ', oldVal)
          //     this.timerCount = newVal
          // },
          // customContent: function (newVal, oldVal) {
          //     console.log('Prop changed: ', newVal, ' | was: ', oldVal)
          //     this.content = newVal
          // },
      }
  }
  
  </script>
  