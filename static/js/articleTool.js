function insertEffect(effect){
    let ex = document.getElementById("experience");
    let text = ex.value;
    let start = ex.selectionStart;
    let end = ex.selectionEnd;
    final = text.substring(0,start) + `<${effect}>` + text.substring(start, end) + `</${effect}>` + text.substring(end)
    ex.value = final;
}
function insertEffect2(effect){
    let ex = document.getElementById("experience");
    let text = ex.value;
    let start = ex.selectionStart;
    let later = text.substring(start)
    final = text.substring(0,start) + `</${effect}>` + later
    ex.value = final;
}
// 自動插入<br>標籤
// document.body.addEventListener('keydown',function(event){
//     if(event.key == 'Enter'){
//         let ex = document.getElementById("experience");
//         let start = ex.selectionStart;
//         let text = ex.value;
//         if(start != 0) {
//             final = text.substring(0,start) + `<br>` + text.substring(start)
//             ex.value = final;
//         }
//     }
// });

$(document).ready(function() {
    // 监听颜色选择器的 change 事件
    $("#color").change(function() {
        let color = $(this).val();
        let ex = document.getElementById("experience");
        let text = ex.value;
        let start = ex.selectionStart;
        let end = ex.selectionEnd;
        final = text.substring(0,start) + `<font color="${color}">` + text.substring(start, end) + `</font>` + text.substring(end)
        ex.value = final;
        // $("#experience").append(color);
    });
});