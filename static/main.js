'use Strict';




// filter therapists by county
$(function(){
    $('#select-county').on('submit',function(){
        event.preventDefault();
        var value=$("input[name=county]:checked").val();
        switch(value){
            case "dakota": location.href='/therapists/dakota-county'; break;
            case "hennepin": location.href='/therapists/hennepin-county'; break;
            case "ramsey": location.href='/therapists/ramsey-county'; break;
            case "washington": location.href='/therapists/washington-county'; break;
        }
    });
});