$(document).ready( function () {

  if (jQuery) {
    console.log("jQuery esta cargado");
    } else {
      console.log("jQuery no esta cargado");
   };

   $('#tablag').DataTable( {
       buttons: [
           'copy', 'excel', 'pdf'
       ]
   } );


}); //end document ready
