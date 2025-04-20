function check_passwords() {
  let password = document.getElementById("password").value;
  let check_password = document.getElementById("check_password");
  
  
  if (password.length >= 8) {
    check_password.style.color="#20c997";
    check_password.innerHTML = "Mot de passe OK";
  }
  else {
    check_password.style.color="#dc3545";
    check_password.innerHTML = "8 caractères minimum"
  }
}
