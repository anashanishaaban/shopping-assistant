/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui"),require('@tailwindcss/forms'),],
  daisyui:{
    themes:["light","dark","cupcake"]
  }
}

