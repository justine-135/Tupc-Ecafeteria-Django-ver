window.addEventListener('load', ()=>{
    $("input:checkbox").each(function() {
        var value = $(this).attr('value'); // grab value of original
        var ischecked = $(this).is(":checked"); //check if checked

        $(this).change(function() {
            console.log($(this).val())
            $(this).attr('value', this.checked ? "True" : "False")
          })
       });
})