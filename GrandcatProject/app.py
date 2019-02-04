<!DOCTYPE html>
<html>
    
    
    <meta charset="utf-8" />
    <title>GrandPY</title>
    
            
    <style type="text/css">
    
        h1{
            text-align:center;
        }
        
        h2{
            text-align:center;
        }


        .image1{
            border="6";
            border-radius:8px;
        }

        .menu{
            position:relative;
            left:2500px;
        }

        h3{
            text-align:center;
            font-style:italic;
        }

        .div{
            position:relative;
            left:275px;
            style="width:600px;
            height:300px;
            border:2px solid #999999;
            text-align:center;
        }

        form{
            text-align:center;
        }
       
        p{
            text-align:center;
        }

        #blockinput{
            text-align:center;
        }

        #input{
            text-align:center;
            font-style:italic;
        }


        .div{
            margin-top:-200px;
            text-align:center;
            border:2px solid black;
            width: 580px;
            height: 300px;
            background-color:pink;
            overflow:scroll;
        }


        #map{
        
            height:200px;
            width:20%;
            margin-left:900px;
            top:0px;
            position: fixed
        }



        #image1{
            margin-top:auto;
            margin-left:910px;
        }




    </style>



    <head>

    
        <img src="/static/images/image1.jpg" class="image1" alt="logo"/>

           
        <h1>HOME</h1>
        <h2>Hey I'm GrandCat</h2>
        <h3>Site exclusivement réservé à la recherche d'adresse</h3>


        <ul>
            <li><a href="pages/inscription.html">S'inscrire</a></li>
            <li><a href="pages/contact.html">Contact</a></li>
            <li><a href="pages/about.html">About</a></li>
        </ul>


        <div id="image1"><img src="static/images/tourne/one.jpg"/></div>        

        
    </head>


    <body>

        dzad
        <div id="output"></div>
        dzd


        
       







        
        {{ a }} {{ b }} {{ c }}
        <div id="map"></div>

   


        <br><br><br><br><br><br><br><br><br><br><br><br><br>
        <div class="div">
        
                        
            <div id="monCadre"> {{ a }} {{ b }} {{ c }}</div>  
        </div>

       <div id="monCadre3">dedfz</div>  
        </div>



     <form id="toto" name = "titi" return false;>

        <input type="text" id="input" size="100" name="input"
            placeholder="Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"/><br>


             
        <input type="submit" id="sub_input" name="sub" value="Enter"/>

        
        <input type="button" id="button_input" name="bubu" value="Enter" />

        

    </form>


    <p><img src="/static/images/chat_home.jpg" alt="imagecat" /></p>


    


    <div id="result"></div>  



        <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCt2O8fe5cHDLkjjFk4TQ9Os5Y3vFGmqU8&callback=initMap">
        </script>

    </body>
    
  
  <script
  src="https://code.jquery.com/jquery-3.3.1.js"
  integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
  crossorigin="anonymous"></script>    <script type = "text/javascript">


    $("#output").load("/static/images/requete.txt", "requete.txt");


    $('form').on('submit',function(event){
        event.preventDefault();
        var a = document.getElementById("input").value;
        $.post('/registration', {"test":a});
        message();
        effacer();
    });


    
    
    var a = {"test":a};





    function readFile(){
        jQuery.get("requete.txt", function(txt){
            $("output").text(txt);
        });
    }






















        
    $('#monCadre3').load('requete.txt');
 






        
        function image_tourne(){
            var liste = [
                "one.jpg",
                "two.jpg",
                "three.jpg",
                "for.jpg",
                "five.jpg"
                ];
        document.getElementById("image1").innerHTML = `<img src="static/images/tourne/${liste[4]}" />`;
            for(var i = 0; i >= liste.length; i++){
                
                document.getElementById("image1").innerHTML = `<img src="static/images/tourne/${liste[4]}" />`;
            };
        };

        setTimeout(image_tourne(),500);




        function initMap(){
            var options = {
                zoom:13,
                center:{lat:44.7167,lng:5.05}
            }
            var map = new google.maps.Map(document.getElementById("map"), options);
        } 
         


        var historic = []
        function message(){
            const recup = document.getElementById("input").value;
            var path =` https://www.google.com/maps/search/${recup}`;
            historic.push(recup+"<br>");
            document.getElementById("monCadre2").innerHTML = historic.join("");
            effacer();
          
        };




        function effacer(){
            document.getElementById("input").value = "";
        }







        function imageTourne(){
            document.getElementById('nom-de-ta-photo').src= "l'url de ta nouvelle image";
        }
    </script>




































    
