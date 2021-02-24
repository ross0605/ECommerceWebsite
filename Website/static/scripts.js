 // $(document).ready(function() {
 //            $(".menu-icon").on("click", function() {
 //                  $("nav ul").toggleClass("showing");
 //            });
 //      });

 //      // Scrolling Effect

 //      $(window).on("scroll", function() {
 //            if($(window).scrollTop()) {
 //                  $('nav').addClass('black');
 //            }

 //            else {
 //                  $('nav').removeClass('black');
 //            }
 //      })



// function for flipping image on home page
function toggleImage(imageNumber, image1) {
   var img1 = image1;
   
   var imgElement = document.getElementById('image' + imageNumber);

   var IG = imgElement.src;

   var Path = IG.split('/static/', 2);
   Path[1] = Path[1];


   imgElement.src = img1;


   // imgElement.src = (Path[1] === img1)? img2 : img1;

}

// function for flipping image on home page
function toggleImage2(imageNumber, image1) {
   var img1 = image1;
   
   var imgElement = document.getElementById('image' + imageNumber);

   var IG = imgElement.src;

   var Path = IG.split('/static/', 2);
   Path[1] = Path[1];


   imgElement.src = img1;


   // imgElement.src = (Path[1] === img1)? img2 : img1;

}


function show_selected(idVar) {
  var idV = idVar;

    var x = document.getElementById("selectID").selectedIndex;
  var y = document.getElementsByTagName("option")[x].value;
  var z = '1';
  
  window.location.href=/addtocart/+idV+"/"+y+"/"+"1";
}
