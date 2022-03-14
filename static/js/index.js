// function checkURL(str){
//     if (str.match(/https?:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#\u3000-\u30FE\u4E00-\u9FA0\uFF01-\uFFE3]+/g) == null) {
//         console.log(false);
//         return false
//     }
//     else {
//         console.log(true);
//         return true;
//     }
// }

// urlText = document.getElementById("urlText")
// goButton = document.getElementById("goButton")

// urlText.addEventListener("input", function(){
//     if(checkURL(urlText.value)){
//         goButton.removeAttribute("disabled")
//     }else{
//         goButton.setAttribute("disabled","")
//     }
// })

// goButton.addEventListener("mousedown",function(){
//     if(goButton.hasAttribute("disabled")){
//         alert("URLを入力してください。")
//     }
// })