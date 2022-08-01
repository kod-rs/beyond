// module.exports = {
//   publicPath: process.env.NODE_ENV === "production" ? "/beyond/" : "/",
//   // configureWebpack: config => {

//   //   // if (process.env.NODE_ENV === 'production') {
//   //   if (process.env.ENVIRONMENT === 'DEVELOPMENT') {
//   //     // mutate config for production...
//   //     console.log("dev")
//   //   } else {
//   //     console.log("production")
//   //     // mutate for development...
//   //   }
//   // }

// };

const path = require("path");

console.log("vue config ")

module.exports = {
  assetsDir: "./src_vue",

  chainWebpack: config => {
    config
      .entry("app")
      .clear()
      .add("./src_vue/index.js")
      .end();
    config.resolve.alias
      .set("@", path.join(__dirname, "./src_vue"));
    config
      .plugin('html')
      .tap(args => {
        args[0].template = '/src_vue/template/index.html'
        return args
      })
  },

  // chainWebpack: config => {
  //   config
  //     .plugin('html')
  //     .tap(args => {
  //       args[0].template = '/Users/username/proj/app/templates/index.html'
  //       return args
  //     })
  // }

  publicPath: process.env.NODE_ENV === "production" ? "/beyond/" : "/",

};
