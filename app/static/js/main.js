//DOM Selection
const copyBtn = document.getElementById("copyBtn");
const shortURL = document.getElementById("shortURL")


//Event Listeners
copyBtn.addEventListener("click", handleCopyText)




//Functions
function handleCopyText(){
    shortURL.select();
    shortURL.setSelectionRange(0, 99999); /* For mobile devices */
    navigator.clipboard.writeText(shortURL.value);
    console.log("content copied!")
}
