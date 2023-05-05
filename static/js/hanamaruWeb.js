new WOW().init();


$(document).ready(function() {
    let width = $("#markdown").width();
    $("#translation").width(width+50);

    $(document).mousemove(function() {
        let height = $('#markdown').height();
        $("#translation").height(height+10);
    });

    $(window).on("resize", function() {
        let width = $("#markdown").width();
        $("#translation").width(width+50);
      });
  });

let typed = new Typed('.typer', {
    strings: ['歡迎來到，', '沒事有事都會維護的神奇網站'],
    typeSpeed: 80,
}); // https://unpkg.com/typed.js@2.0.16/dist/typed.umd.js


function cl(){
    let converter = new showdown.Converter();
    let md = document.getElementById("markdown").value;
    let html = converter.makeHtml(md);
    console.log(html);
    document.getElementById("translation").innerHTML = html;
    }

function insertMarkdown(element){
    let input = document.getElementById("markdown");
    let text = input.value;
    let start = input.selectionStart;
    let end = input.selectionEnd;
    if(element == '```'){
        final = text.substring(0,start) + element + text.substring(start, end) + '\n' + element + text.substring(end);
    }else if(element == '* '){
        final = text.substring(0,start) + element + text.substring(start, end) + text.substring(end);
    }else{
        final = text.substring(0,start) + element + text.substring(start, end) + element + text.substring(end);
    }
    input.value = final;
    }
function insertHasendtag(effect){
    let ex = document.getElementById("markdown");
    let text = ex.value;
    let start = ex.selectionStart;
    let end = ex.selectionEnd;
    final = text.substring(0,start) + `<${effect}>` + text.substring(start, end) + `</${effect}>` + text.substring(end)
    ex.value = final;
    }
function insertWithoutendtag(effect){
    let ex = document.getElementById("markdown");
    let text = ex.value;
    let start = ex.selectionStart;
    let later = text.substring(start)
    final = text.substring(0,start) + `</${effect}>` + later
    ex.value = final;
}

$(document).ready(function() {
    // 监听颜色选择器的 change 事件
    $("#color").change(function() {
        let color = $(this).val();
        let ex = document.getElementById("markdown");
        let text = ex.value;
        let start = ex.selectionStart;
        let end = ex.selectionEnd;
        final = text.substring(0,start) + `<font color="${color}">` + text.substring(start, end) + `</font>` + text.substring(end)
        ex.value = final;
        // $("#experience").append(color);
    });
});