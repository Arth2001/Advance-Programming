function login(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "arth" && password === "arth") {
        window.location.href = "index.html"
    }else{
        alert("Invalid username or password")

    }

}



function logout(){
    window.location.href = "login.html"
}