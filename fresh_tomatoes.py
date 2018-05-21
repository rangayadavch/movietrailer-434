#!/usr/bin/env python


import webbrowser
import os
import re
# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Movie trailers</title>

   <style>

    .modal {
    display: none;
    position: fixed;
    z-index: 1;
    padding-top:100px;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0,0,0);
    background-color: rgba(0,0,0,0.4);
}


.modal-content {
    margin: 5% auto;
    padding: 20px;
    width: 80%;
    min-height:500px;
}

/* The Close Button */
.close {
    color: #aaa;
    float: right;
    font-size: 30px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    background-color: black;
    text-decoration: none;
    cursor: pointer;
    padding-left:5px;
    padding-right:5px;
}

      .container{
        display: flex;
        flex-wrap:wrap;
        font-family:arial,cursive;
       }
     .box{
          width:100%;
          min-height:150px;
          cursor:pointer;
        }
      @media screen and (min-width :450px)  {
      div.r1:hover{
             border:1px;
             background-color:gray;
             }
       div.r2:hover{
             border:1px;
             background-color:black;
             }
       div.r3:hover{
             border:1px;
             background-color:blue;
             }
       div.r4:hover{
             border:1px;
             background-color:red;
             }
      div.r5:hover{
             border:1px;
             background-color:skyblue;
             }
       .r1{width:50%;}
       .r2{width:50%;}
       .r3{width:50%;}
       .r4{width:50%;}
       .r5{width:50%;}
       h1 {background-color:black;}
        }
      h1 {background-color:orange;
         font-family:arial,cursive;}
      </style>
      <div>
      <!-- The Modal -->
         <div id="myModal" class="modal">

  <!-- Modal content -->
           <div class="modal-content">
                <span class="close">&times;</span>
                 <iframe id="f" width="70%" height="315" {movie_tiles} src=""
                        frameborder="0" allow="autoplay;
                        encrypted-media" allowfullscreen></iframe>
          </div>
        </div>
</div>
   <script>

var modal = document.getElementById('myModal');


var span = document.getElementsByClassName("close")[0];


    onc = function(c) {
    modal.style.display = "block";
    c='https://www.youtube.com/embed/'+c;
    console.log(c);
    document.getElementById("f").setAttribute("src",c);
}
    span.onclick = function() {
        modal.style.display = "none";
}


   window.onclick = function(event) {
       if (event.target == modal) {
          modal.style.display = "none";
    }
}
</script>
</head>
'''
# Main page layout
main_page_content = '''
<body style="text-align:center">
   <h1 style="color:white">MOVIE TRAILERS</h1>
   <div class="container">
   <div class="box r1" onclick="onc('sOEg_YZQsTI')">
        <img vspace="30" src="https://bit.ly/2GBNgc1" style="width:70%"
            height="300" hspace="30";>
        <h2 style="color:white;">Bahubali</h2></div>
   <div class="box r2" onclick="onc('6ZfuNTqbHE8')">
        <img vspace="30" src="https://bit.ly/2rnOhQx"
            style="width:60%" height="300" hspace="30">
        <h2 style="color:white;">Avengers war</h2></div>
   <div class="box r3" onclick="onc('7nhUXE41IfQ')">
        <img vspace="30" src="https://bit.ly/2IYFqP5"
            style="width:60%" height="300" hspace="30">
        <h2 style="color:white;">Gang</h2> </div>
   <div class="box r4" onclick="onc('V4KdbX1xvaI')">
        <img vspace="30" src = "https://bit.ly/2GzwQAZ"
            style="width:60%" height="300"  hspace="30">
                <h2 style="color:white;">a aa</h2></div>
   <div class="box r5" onclick="onc('i4SkO3ypCXw')">
        <img vspace="30" src="https://bit.ly/2ICFF2T"
            style="width:60%" height="300" hspace="30">
        <h2 style="color:white;">Drunken Master</h2></div>

</body>

</html>
'''
movie_head_content = '''
<div class="col-md-6 col-lg-4 movie-title text center" data-trailer-youtube-
  id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
     <h2 style="color:white;">{movie_title}</h2>
   </div>
   '''


def create_movie_heads_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_head_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_heads=create_movie_heads_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
