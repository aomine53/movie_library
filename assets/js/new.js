function movieListApiCall(pagenum) {
    let api_obj = {};
    let types = ['movie', 'series', 'episodes'];
    document.getElementById('search').addEventListener('click', (e) => {
      document.getElementById('movie_list').innerHTML = "";
      api_obj = {};
      console.log(document.getElementById('title').value);
      let title = document.getElementById('title').value;
      let year = document.getElementById('year').value;
      let type = document.getElementById('type').value;
      let typer = types[parseInt(type) - 1];
      console.log(title + " " + year + " " + types[parseInt(type) - 1]);
      console.log(type);
      api_obj['apikey'] = '4cf0ae48';
      api_obj['page'] = parseInt(pagenum);
      if (title != '') {
        api_obj['s'] = title;
      }
      if (year != '') {
        api_obj['y'] = year;
      }
      if (typer != undefined) {
        api_obj['type'] = typer;
      }
      // console.log(api_obj);
      fetch('http://www.omdbapi.com/?' + new URLSearchParams(api_obj)).then(response => response.json())
        .then(data => {
  
          console.log(data);
          if (data.Response == "True") {
            data.Search.forEach(element => {
              document.getElementById('movie_list').innerHTML += `<div class="col-lg-3 mb-4 mt-2">
      <div class="card">
          <img class="card-img-top" width="100" height="400" src="${element.Poster}" alt="Image Not Loading">
          <div class="card-body" onclick="showMoreInfo('${element.imdbID}')">
              <h5 class="card-title">${element.Title}</h5>
              <ul class="list-group list-group-flush">
              <li class="list-group-item"><b>IMDb ID</b> : ${element.imdbID}</li>
              <li class="list-group-item"><b>Year</b> : ${element.Year}</li>
              <li class="list-group-item"><b>Type</b> : ${element.Type}</li>
            </ul>
          </div>
          <div class="card-footer bg-white border-dark d-flex justify-content-around">
          <button class="btn btn-outline-danger"  onclick="addToFavorites('${element.imdbID}')" type="button"><i class="far fa-heart"></i></button>
          <button class="btn btn-outline-info"  onclick="showMoreInfo('${element.imdbID}')" type="button"><i class="fas fa-info-circle"></i></button> 
          </div>
          
      </div>
  </div>`
            })
          }
          else {
            alert("Error : " + data.Error)
          }
        });
    })
  
  }
  movieListApiCall(1);
  var imdbID = "";
  function addToFavorites(id) {
    $("#addtolistmodel").modal("show");
    console.log(id);
    imdbID = id;
  };
  
  function ex(name) {
    $.ajax({
      method: "POST",
      url: "api/addtofavorites",
      async: true,
      data: {
        csrfmiddlewaretoken: csrftoken,
        imdbid: imdbID,
        favorite_list_name: name,
      },
      success: function (result, status, xhr) {
        console.log(result);
        $('#addmodel').modal('hide')
        alert(result.message);
      },
      error: function (error_data) {
        console.log("error");
        alert("error");
        console.log(error_data);
      },
    });
  }
  document.getElementById('close').addEventListener('click', () => {
    $('#addtolistmodel').modal('hide')
  })
  
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  const csrftoken = getCookie("csrftoken");
  
  
  
  
  
  // let pagen = 1;
  // window.addEventListener('scroll', () => {
  //   console.log('scroll');
  
  //   if (
  //     window.scrollY + window.innerHeight >= document.body.offsetHeight
  //   ) {
  //     // setTimeout(movieListApiCall(pagen++), 3000);
  //     console.log('ifscroll');
  //     console.log(pagen);
  //     pagen += 1;
  //     movieListApiCall(pagen)
  //   }
  // });
  
  function showMoreInfo(imdbid) {
    $('#moreinfo').modal('show')
    api_obj = {};
    api_obj['apikey'] = '4cf0ae48';
    api_obj['i'] = imdbid;
    console.log(api_obj);
    fetch('http://www.omdbapi.com/?' + new URLSearchParams(api_obj)).then(response => response.json())
      .then(data => {
        console.log(data.Title)
        document.getElementById('title_name').textContent = data.Title;
        document.getElementById('release_date').innerHTML = `<span class='text-muted'>Release Data : </span>` + data.Released
        document.getElementById('runtime').innerHTML = `<span class='text-muted'>Runtime : </span>` + data.Runtime
        document.getElementById('genre').innerHTML = `<span class='text-muted'>Genre : </span>` + data.Genre
        document.getElementById('director').innerHTML = `<span class='text-muted'>Director : </span>` + data.Director
        document.getElementById('imdb_rating').innerHTML = `<span class='text-muted'>IMDb Rating : </span>` + data.imdbRating
        document.getElementById('poster').src = data.Poster
        document.getElementById('plot').innerHTML = `<span class='text-muted'>Plot : </span>` + data.Plot
  
      }
      );
  }
  
  document.getElementById('close_info').addEventListener('click', () => {
    $('#moreinfo').modal('hide')
  })