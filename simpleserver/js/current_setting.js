$(function(){

$("table.tbl tbody").html("");

    $.getJSON("json/config.json", function(data){
        $(data.list).each(function(){
            $('<tr>'+
            '<th>'+this.id+'</th>'+
            '<td class="label"><span class="' + this.label + '">' +
            this.body + '</span></td>'+
            '</tr>').appendTo('table.tbl tbody');
})
})
});
