


image_selection = d3.selectAll("#b2")
place_img_here = d3.select("#img2")


function uploaded_file(image_name)
{
    urlz = `/show/${image_name}`
    urls = `/uploads/${image_name}`/// API ADDRESS USE COUNTRY NAME AS QUERY 
 
    // d3.json(urlz).then(function(x) {
    // d3.json(urlz);



    // window.history.pushState( urlz);
    // window.history.pushState( "Recipe-O-Matic", '/show/chief1.jpg');

    console.log('the image name is' , image_name)


    // var image_pic = d3.request( urlz )
    // d3.request( urls );
    // d3.call( urls );
    // d3.json( urlz ).then(function(response)
    // {
    //    var test = response ;
    //    console.log("this is the response", response);

  

    //  var test = d3( urlz );
  
    // // place_img_here.append(image_pic)
    // console.log('print get_image name',  image_name );
}


image_selection.on("change", function()
// image_selection.on("click", function()
{
//    var image_name = image_selection.attr("DOMString")
//    var image_name = image_selection.attr(".html")
   var image = image_selection.selectAll()
   console.log("the image name is", image._parents[0].files[0].name );

   image_name = image._parents[0].files[0].name 
  //  url = 'http://127.0.0.1:5000/show/'+image_name
    //  url = '{{url_for(/show/'+image_name+')}}'
     url = 'url_for(/show/'+image_name

    //  url = '..images/'+image_name
  //  url = 'http://www.cnn.com'


   console.log('the url is:', url);

   d3.select("#b3")
   //  .append('href=')
     //  b.select("href")
     .attr('href', url)
     .attr('action', url)

  
 

  // d3.select("#img1")
  // //  .append('href=')
  //   //  b.select("href")
  //   // .attr('href', url)
  //   // .attr('action', url)
  //   .attr('scr', url)
    // .attr('scr', url)

   

  // get_image( image_name);
});
//  uploaded_file('robot2.jpg');


//  get_image('robot2.jpg');
// window.history.pushState( "Recipe-O-Matic", '/show/chief1.jpg');




// list_builder();

// function confirmed_ingres()
//   {
//   confirm_ingred = ['bogus ingred', 'hotdog', 'bun', 'pickles'];
//   // var names = d3.select('.form1').selectAll('input').attr("value")
//   // var names = d3.select('#form1').selectAll('input').select("innerHtml")
//   // var names = d3.select('#form1').selectAll('input').select("label")
//  d3.select('#form1')
//     .data(confirm_ingred)
//     // .enter()
//     .append("input")
//     .attr("type", "checkbox")
//     .attr("value", data => data )
//     .attr("name",  data => data )
//     .attr("text", data => data )
//     .attr("label", data => data) 
//     // .append("br")

//     .html(function(d){
//       return ` ${d} ` 
//       });
//     // .html(function(d){
//     //   return ` <br>` ;
//     //   });
//   }


  // input_group.selectAll('input')
  // .append("label")
  // .text("Your Mom")
  // .html("'YOUR' 'LABEL'")


  function confirmed_ingres( ingres_list)
    {
      var confirm_ingred = ['bogus ingred', 'hotdog', 'bun', 'pickles'];

      confirm_ingred.map(( x ) =>
            {
                var inputz = d3.select('#form1')
                inputz.append('br') // PUTS A SPACE BETWEEN EACH CHECK BOX
                
                inputz.append("input")
                .attr("type", "checkbox")
                .attr("id", x)
                .attr("value", x )
                .attr("name",  x )

                inputz.append('label') // INSERTS A LABEL ON SAME LINE AS CHECK BOX
                .html(`--${x}`) // THIS IS THE TEXT OF OUR LABEL
                .style('font-weight', 'bold') // THIS MAKES TEXT BOLD 
              }
            );

        d3.select('#form1')  // GIVE US ONE LINE BREAL
          .append('br')

        d3.select('#form1') // CREATE THE SUBMIT BUTTON
          // .html(`<br>`)
          .append('input')
          .attr('type', 'submit')
          .attr('id', 'submit1')
          .attr('value', 'Submit')
      } 


confirmed_ingres() ;

function list_builder2()
{
    var ingreds = ['bogus ingred', 'hotdog', 'bun', 'pickles'];
    ingreds.map(( x ) =>
          {
          var t= d3.select('.article')
            t.append('li').html(x)
            // .html(x)
          }
      );
}

list_builder2();

// 0: input#b2
// accept: ""
// alt: ""
// autocomplete: ""
// defaultChecked: false
// checked: false
// dirName: ""
// disabled: false
// form: form
// acceptCharset: ""
// action: "http://127.0.0.1:5000/?myFile.x=280&myFile.y=34#"
// autocomplete: "on"
// enctype: "application/x-www-form-urlencoded"
// encoding: "application/x-www-form-urlencoded"
// method: "get"
// name: ""
// noValidate: false
// target: ""
// elements: HTMLFormControlsCollection(2)
// length: 2
// 0: input#b2
// accept: ""
// alt: ""
// autocomplete: ""
// defaultChecked: false
// checked: false
// dirName: ""
// disabled: false
// form: form
// files: FileList
// length: 1
// 0: File
// name: "robot1.jpg"
// lastModified: 1578284310585
// lastModifiedDate: Sun Jan 05 2020 20:18:30 GMT-0800 (Pacific Standard Time) {}
// webkitRelativePath: ""
// size: 92408
// type: "image/jpeg"
// __proto__: File