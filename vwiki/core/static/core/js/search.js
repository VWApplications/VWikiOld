function searchSites() {
  var input, ul;
  input = document.getElementById('searchInput');
  ul = document.getElementById("searchUL");
  search(ul, input)
}

function search(ul, input) {
  var filter, li, a, i;
  filter = input.value.toUpperCase();
  li = ul.getElementsByTagName('li');
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("a")[0];
    if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
