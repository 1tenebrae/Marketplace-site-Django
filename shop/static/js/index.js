function myFunction() {
    document.getElementById("myDropdown").classList.toggle("menu-active");
}

window.onclick = function(event) {
    if (!event.target.matches('.dropdown-toggle')) {
  
      var dropdowns = document.getElementsByClassName("dropdown-menu");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('menu-active')) {
          openDropdown.classList.remove('menu-active');
        }
      }
    }
  } 

  