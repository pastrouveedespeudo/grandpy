var liste_image_logo = ["/static/images/loading/one.jpg",
                      "/static/images/loading/two.jpg",
                      "/static/images/loading/one.jpg",
                      "/static/images/loading/two.jpg",
                      "/static/images/loading/one.jpg",
                      "/static/images/loading/two.jpg",
                      "/static/images/loading/three.jpg"];


var liste_image_logo_i = 0

function change_image(){
document.getElementById('tourne').src = liste_image_logo[liste_image_logo_i];
if(liste_image_logo_i < liste_image_logo.length - 1){
  liste_image_logo_i++
}
else{
  liste_image_logo_i = 0
}
};



var time;
function start_logo_loading(){
time = window.setInterval("change_image()", 1000);
}


function stop_logo_loading(){
clearTimeout(time);
}








$(document).ready(function(){
$("#formPseudo").on("submit", function(ev){

$.ajax({
  data:{
    data:$("#idRecupPseudo").val(),
  },
  type:"POST",
  url:"/login"


})
.done(function(data){

  if (data.error){
      $("#monCadreAlert").text(data.error);
      $("#divPseudo");
  }
  else{
      $("#divPseudo").html(data.data);
      $("#monCadreAlert");
      alert("fini")
      
      
  }


  });
  map();
  effacer();
  ev.preventDefault();

});
});


function map(){


document.getElementById("map").innerHTML = ""
document.getElementById("map").style.width = "580px"
}









MONCADRE = []

$(document).ready(function(){
  
  $("form").on("submit", function(e){
      start_logo_loading();
      $.ajax({
          data:{
              data:$("#idRecupInfo").val(),

          },
          type:"POST",
          url:"/data"

          

      })
      .done(function(data){

          if (data.error){
              $("#monCadreAlert").text(data.error);
              $("#monCadre");
          }
          else{
              $("#monCadre").html(data.data);
              $("#monCadreAlert");
              initMap();
              
          };


      });
      
      
      add_favorite();
      e.preventDefault();
      map();
      
  });
});




MONCADRE_WKI = []

$(document).ready(function(){
  var finish2 = []
  $("form").on("submit", function(ev){

      $.ajax({
          data:{
              data:$("#idRecupInfo").val(),

          },
          type:"POST",
          url:"/wiki"
          

      })
      
      .done(function(data){

          if (data.error){
              $("#monCadreAlert").text(data.error);
              $("#monCadreWiki");
          }
          else{
              $("#monCadreWiki").html(data.data);
              $("#monCadreAlert");
              stop_logo_loading();
              
          }
      });
      
      effacer();
      ev.preventDefault();
  
  });
});





function add_favorite(){
var ask = '  <center>Voulez vous ajouter cette adresse à vos favoris ?</center> \
            <form> \
            <input type="submit" class="classButtonInput" id="idButtonInput" value="Oui"/> \
            <input type="submit" class="classButtonInput" id="idButtonInput" value="Non"/> \
            <form>'


document.getElementById("divFavorite").innerHTML = ask
//ici faire un post
//et document.getElementById("divFavorite").innerHTML = ""

};




function initMap(){
  
  liste = [[],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[]]
  
  liste2 = []
  
  var c = document.getElementById("monCadre");
  var a = c.innerText || c.textContent;
  var b = a.length;
  //console.log(a)
  
  var c = 0;

  for(var i = 0; i<=b;i++){
    liste[c].push(a[i]);
    if(a[i] === ","){
        c++;
        };
  };

  for(var i =0;i<=liste.length;i++){
      if(liste[i]!=""){
          liste2.push(liste[i]);
      }
   };
  //console.log(liste2)
  a = Number(liste2[liste2.length -3].slice(1,-1).join(''));
  b = Number(liste2[liste2.length -2].slice(2,-5).join(''));
  //console.log(liste2)
  //console.log(a)
  //console.log(b)
  //console.log(liste2.length -2)


  var options = {
      zoom:13,
      center:{lat:a,lng:b}
  }
  var map = new google.maps.Map(document.getElementById("map"), options);
} 





function effacer(){
  document.getElementById("idRecupInfo").value = "";
}



function imageTourne(){
  document.getElementById('nom-de-ta-photo').src= "l'url de ta nouvelle image";
}


